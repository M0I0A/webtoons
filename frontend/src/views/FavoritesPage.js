import React, { useEffect, useState } from 'react';
import axios from 'axios';

const FavoritesPage = () => {
    const [favorites, setFavorites] = useState([]);
    const [error, setError] = useState(null); // State for error handling
    const userId = localStorage.getItem('user_id'); // Get the user ID from local storage

    useEffect(() => {
        const fetchFavorites = async () => {
            if (!userId) {
                setError('User ID is not available. Please log in.');
                return;
            }
            try {
                const response = await axios.get(`http://localhost:8000/api/users/${userId}/favorites/`, {
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('access_token')}` // Use your auth method
                    }
                });
                setFavorites(response.data);
            } catch (err) {
                setError(err); // Set error state
            }
        };

        fetchFavorites();
    }, [userId]);

    if (error) {
        return <div>Error fetching favorites: {error}</div>;
    }

    return (
        <div>
            <h2>Your Favorite Webtoons</h2>
            <ul>
                {favorites.map(favorite => (
                    <li key={favorite.id}>
                        {favorite.webtoon.title} {/* Adjust as per your favorite model */}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default FavoritesPage;
