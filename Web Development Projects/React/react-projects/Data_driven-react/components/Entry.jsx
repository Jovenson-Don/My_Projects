export default function Entry(props) {
    return (
        <article className="journal-entry">
            <div className="main-image-container">
                <img 
                    className="main-image"
                    src={props.data.img.src} 
                    alt={props.data.img.alt}
                />
            </div>
            <div className="info-container">
                <img 
                    className="marker"
                    src="../images/marker.png" 
                    alt="map marker icon"
                />
                <span className="country">{props.data.country}</span>
                <a href={props.data.googleMapsLink} target="_blank">View on Google Maps</a>
                <h2 className="entry-title">{props.data.title}</h2>
                <p className="trip-dates">{props.data.dates}</p>
                <p className="entry-text">{props.data.text}</p>
            </div>
            
        </article>
    )
}