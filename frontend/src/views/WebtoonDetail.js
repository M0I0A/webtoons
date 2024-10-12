import React, { useState, useEffect } from 'react';
import axios from 'axios';

const WebtoonDetail = ({ match }) => {
    const [webtoon, setWebtoon] = useState({});
    const [isFavorited, setIsFavorited] = useState(false);
    const [comments, setComments] = useState([]);
    const [newComment, setNewComment] = useState('');

    useEffect(() => {
        const fetchWebtoon = async () => {
            try {
                const response = await axios.get(`http://localhost:8000/api/webtoons/${match.params.id}/`);
                setWebtoon(response.data);
                checkFavorite(response.data.id); // Check if this webtoon is already favorited
                fetchComments(response.data.id); // Fetch comments for this webtoon
            } catch (error) {
                console.error('Error fetching webtoon details:', error);
            }
        };

        fetchWebtoon();
    }, [match.params.id]);

    const checkFavorite = async (webtoonId) => {
        try {
            const response = await axios.get('http://localhost:8000/api/favorites/', {
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem('access_token')}` // Use your auth method
                }
            });
            const favoriteExists = response.data.some(fav => fav.webtoon.id === webtoonId);
            setIsFavorited(favoriteExists);
        } catch (error) {
            console.error('Error checking favorites:', error);
        }
    };

    const fetchComments = async (webtoonId) => {
        try {
            const response = await axios.get(`http://localhost:8000/api/webtoons/${webtoonId}/comments/`);
            setComments(response.data);
        } catch (error) {
            console.error('Error fetching comments:', error);
        }
    };

    const handleFavoriteToggle = async () => {
        const url = isFavorited
            ? `http://localhost:8000/api/favorites/remove/${webtoon.id}/`
            : `http://localhost:8000/api/favorites/add/`;

        const method = isFavorited ? 'DELETE' : 'POST';
        const data = !isFavorited ? { webtoon: webtoon.id } : null;

        try {
            await axios({
                method,
                url,
                data,
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem('access_token')}` // Use your auth method
                },
            });
            setIsFavorited(!isFavorited);
        } catch (error) {
            console.error('Error toggling favorite:', error);
        }
    };

    const handleCommentSubmit = async (event) => {
        event.preventDefault();
        try {
            await axios.post(`http://localhost:8000/api/webtoons/${webtoon.id}/comments/`, {
                text: newComment
            }, {
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem('access_token')}` // Use your auth method
                }
            });
            setNewComment(''); // Clear the input field
            fetchComments(webtoon.id); // Refresh comments after submitting
        } catch (error) {
            console.error('Error submitting comment:', error);
        }
    };

    return (
        <div className="container" style={{ paddingTop: '30px' }}>
            <h2>{webtoon.title}</h2>
            <img src={webtoon.thumbnile} alt={webtoon.title} />
            <p><strong>Creator:</strong> {webtoon.creator}</p>
            <p><strong>Genre:</strong> {webtoon.genre}</p>

            <p>{webtoon.description}</p>
            <button onClick={handleFavoriteToggle} className="btn btn-primary">
                {isFavorited ? 'Remove from Favorites' : 'Add to Favorites'}
            </button>

            {/* Comments Section */}
            <div>
                <h3>Comments</h3>
                <ul>
                    {comments.map(comment => (
                        <li key={comment.id}>{comment.text}</li>
                    ))}
                </ul>
                <form onSubmit={handleCommentSubmit}>
                    <input
                        type="text"
                        value={newComment}
                        onChange={(e) => setNewComment(e.target.value)}
                        placeholder="Add a comment..."
                        required
                    />
                    <button type="submit">Submit</button>
                </form>
            </div>
        </div>
    );
};

export default WebtoonDetail;
