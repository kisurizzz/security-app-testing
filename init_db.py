from app import create_app, db
from app.models import SearchableContent
import random

def init_db():
    app = create_app()
    with app.app_context():
        # Create all tables
        db.create_all()
        
        # Check if we already have data
        if SearchableContent.query.first() is None:
            # Car data
            car_data = [
                # Toyota
                ("Toyota Camry 2023", "The 2023 Toyota Camry offers a perfect blend of comfort, reliability, and fuel efficiency. Features include advanced safety systems and a spacious interior."),
                ("Toyota Corolla 2023", "The 2023 Toyota Corolla is a compact sedan known for its excellent fuel economy and low maintenance costs. Perfect for city driving."),
                ("Toyota RAV4 2023", "The 2023 Toyota RAV4 is a versatile compact SUV with impressive cargo space and available hybrid powertrain options."),
                
                # Honda
                ("Honda Civic 2023", "The 2023 Honda Civic combines sporty handling with practical features. Available in sedan and hatchback body styles."),
                ("Honda Accord 2023", "The 2023 Honda Accord offers a premium driving experience with advanced technology features and excellent fuel efficiency."),
                ("Honda CR-V 2023", "The 2023 Honda CR-V is a family-friendly SUV with ample cargo space and comfortable seating for five."),
                
                # Ford
                ("Ford Mustang 2023", "The 2023 Ford Mustang is an iconic muscle car with powerful engine options and aggressive styling."),
                ("Ford F-150 2023", "The 2023 Ford F-150 is America's best-selling pickup truck, offering impressive towing capacity and innovative features."),
                ("Ford Explorer 2023", "The 2023 Ford Explorer is a three-row SUV with powerful engine options and advanced technology features."),
                
                # Tesla
                ("Tesla Model 3 2023", "The 2023 Tesla Model 3 is an all-electric sedan with impressive range and acceleration. Features include Autopilot and a minimalist interior."),
                ("Tesla Model Y 2023", "The 2023 Tesla Model Y is an electric crossover SUV with spacious cargo area and advanced technology features."),
                ("Tesla Model S 2023", "The 2023 Tesla Model S is a luxury electric sedan with exceptional performance and range capabilities."),
                
                # BMW
                ("BMW 3 Series 2023", "The 2023 BMW 3 Series offers a perfect balance of luxury and sportiness with precise handling and premium features."),
                ("BMW X5 2023", "The 2023 BMW X5 is a luxury SUV with powerful engine options and a high-quality interior."),
                ("BMW M3 2023", "The 2023 BMW M3 is a high-performance sports sedan with aggressive styling and track-ready capabilities."),
                
                # Mercedes-Benz
                ("Mercedes-Benz C-Class 2023", "The 2023 Mercedes-Benz C-Class offers luxury features and comfortable ride quality in a compact package."),
                ("Mercedes-Benz GLC 2023", "The 2023 Mercedes-Benz GLC is a luxury compact SUV with elegant styling and advanced technology."),
                ("Mercedes-Benz S-Class 2023", "The 2023 Mercedes-Benz S-Class is the flagship luxury sedan with cutting-edge technology and premium comfort features."),
                
                # Audi
                ("Audi A4 2023", "The 2023 Audi A4 combines luxury and performance with Quattro all-wheel drive and premium interior materials."),
                ("Audi Q5 2023", "The 2023 Audi Q5 is a luxury compact SUV with excellent handling and sophisticated technology features."),
                ("Audi RS e-tron GT 2023", "The 2023 Audi RS e-tron GT is a high-performance electric vehicle with stunning design and impressive acceleration."),
                
                # Porsche
                ("Porsche 911 2023", "The 2023 Porsche 911 is an iconic sports car with precise handling and powerful engine options."),
                ("Porsche Cayenne 2023", "The 2023 Porsche Cayenne is a luxury SUV that combines performance with everyday practicality."),
                ("Porsche Taycan 2023", "The 2023 Porsche Taycan is an all-electric sports car with impressive range and track capabilities."),
                
                # Lexus
                ("Lexus RX 2023", "The 2023 Lexus RX is a luxury SUV known for its reliability and comfortable ride quality."),
                ("Lexus ES 2023", "The 2023 Lexus ES is a premium sedan with a quiet cabin and smooth ride characteristics."),
                ("Lexus LC 2023", "The 2023 Lexus LC is a luxury coupe with striking design and powerful performance."),
                
                # Chevrolet
                ("Chevrolet Corvette 2023", "The 2023 Chevrolet Corvette is a mid-engine sports car with supercar performance at an accessible price."),
                ("Chevrolet Silverado 2023", "The 2023 Chevrolet Silverado is a full-size pickup truck with strong towing capacity and modern features."),
                ("Chevrolet Tahoe 2023", "The 2023 Chevrolet Tahoe is a large SUV with three rows of seating and impressive cargo space.")
            ]
            
            # Add all items to the database
            for title, description in car_data:
                db.session.add(SearchableContent(
                    title=title,
                    description=description
                ))
            
            # Commit the changes
            db.session.commit()
            print("Database initialized with car data!")
        else:
            print("Database already contains data!")

if __name__ == '__main__':
    init_db() 