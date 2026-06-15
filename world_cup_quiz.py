"""
Assignment 3: Real world application of loop control statements
World Cup 2026 Winner Predictor using break, continue, and pass statements
"""

# Top 10 World Cup contending countries with their strengths
TOP_10_COUNTRIES = {
    "1": {
        "name": "Argentina",
        "wins": 3,
        "finals": 5,
        "strength": 95,
        "recent_form": "Excellent",
        "description": "Defending champions with strong squad"
    },
    "2": {
        "name": "France",
        "wins": 2,
        "finals": 3,
        "strength": 93,
        "recent_form": "Very Good",
        "description": "Consistent performers, excellent depth"
    },
    "3": {
        "name": "Brazil",
        "wins": 5,
        "finals": 7,
        "strength": 92,
        "recent_form": "Very Good",
        "description": "Most successful nation, always competitive"
    },
    "4": {
        "name": "Germany",
        "wins": 4,
        "finals": 8,
        "strength": 90,
        "recent_form": "Good",
        "description": "Traditional powerhouse with strong youth"
    },
    "5": {
        "name": "Spain",
        "wins": 1,
        "finals": 2,
        "strength": 88,
        "recent_form": "Good",
        "description": "Technical excellence and possession play"
    },
    "6": {
        "name": "England",
        "wins": 1,
        "finals": 2,
        "strength": 87,
        "recent_form": "Good",
        "description": "Young talented squad with promising future"
    },
    "7": {
        "name": "Belgium",
        "wins": 0,
        "finals": 1,
        "strength": 85,
        "recent_form": "Fair",
        "description": "Strong midfield and attacking options"
    },
    "8": {
        "name": "Netherlands",
        "wins": 0,
        "finals": 3,
        "strength": 84,
        "recent_form": "Good",
        "description": "Quality players with attractive style"
    },
    "9": {
        "name": "Italy",
        "wins": 4,
        "finals": 6,
        "strength": 82,
        "recent_form": "Fair",
        "description": "Defensive strength and midfield control"
    },
    "10": {
        "name": "Mexico",
        "wins": 0,
        "finals": 0,
        "strength": 80,
        "recent_form": "Fair",
        "description": "CONCACAF leaders with consistent performances"
    }
}


def display_menu():
    """Display the main menu options."""
    print("\n" + "=" * 60)
    print("         FIFA WORLD CUP 2026 WINNER PREDICTOR")
    print("=" * 60)
    print("\n1. View Top 10 Countries")
    print("2. Predict the Winner")
    print("3. Compare Two Countries")
    print("4. Ranking Analysis")
    print("5. Exit")
    print("\n" + "-" * 60)


def view_countries():
    """Display all top 10 countries with their details."""
    print("\n" + "=" * 60)
    print("TOP 10 WORLD CUP CONTENDING COUNTRIES")
    print("=" * 60)
    
    for rank, country_data in TOP_10_COUNTRIES.items():
        print(f"\nRank {rank}: {country_data['name']}")
        print(f"  Previous Wins: {country_data['wins']}")
        print(f"  Finals Appearances: {country_data['finals']}")
        print(f"  Strength Rating: {country_data['strength']}/100")
        print(f"  Recent Form: {country_data['recent_form']}")
        print(f"  Description: {country_data['description']}")


def predict_winner():
    """Interactive winner prediction with user choices."""
    print("\n" + "=" * 60)
    print("WORLD CUP WINNER PREDICTION")
    print("=" * 60)
    
    predictions = []
    prediction_count = 0
    max_predictions = 3
    
    while True:
        if prediction_count >= max_predictions:
            print(f"\nYou've made {max_predictions} predictions!")
            break  # BREAK statement - exit loop when max predictions reached
        
        print(f"\nPrediction {prediction_count + 1}/{max_predictions}")
        print("\nSelect a country (1-10):")
        
        for rank in range(1, 11):
            country = TOP_10_COUNTRIES[str(rank)]
            print(f"  {rank}. {country['name']}")
        
        print("  0. Cancel predictions")
        
        # Input validation loop
        while True:
            choice = input("\nEnter your choice: ").strip()
            
            if choice == "0":
                print("Cancelling predictions...")
                return predictions  # Exit function
            elif choice in TOP_10_COUNTRIES:
                break  # BREAK statement - valid input received
            else:
                print("Invalid choice. Please enter a number between 1 and 10.")
                continue  # CONTINUE statement - retry input
        
        country_name = TOP_10_COUNTRIES[choice]["name"]
        prediction_number = prediction_count + 1
        predictions.append({
            "rank": prediction_number,
            "country": country_name,
            "strength": TOP_10_COUNTRIES[choice]["strength"]
        })
        
        print(f"✓ Added {country_name} as Prediction #{prediction_number}")
        prediction_count += 1
        
        # Ask if user wants to continue predicting
        while True:
            continue_choice = input("\nAdd another prediction? (yes/no): ").strip().lower()
            
            if continue_choice in ["yes", "y"]:
                break  # BREAK statement - continue predicting
            elif continue_choice in ["no", "n"]:
                print("\nGenerating prediction summary...")
                prediction_count = max_predictions  # Set to max to exit outer loop
                break  # BREAK statement - stop predicting
            else:
                print("Please enter 'yes' or 'no'.")
                continue  # CONTINUE statement - retry input
    
    # Display predictions summary
    if predictions:
        display_predictions(predictions)
    
    return predictions


def display_predictions(predictions):
    """Display the user's predictions."""
    print("\n" + "=" * 60)
    print("YOUR WORLD CUP PREDICTIONS")
    print("=" * 60)
    
    for pred in predictions:
        print(f"\nPrediction #{pred['rank']}: {pred['country']}")
        print(f"  Strength Rating: {pred['strength']}/100")
    
    # Calculate average strength
    total_strength = sum(p['strength'] for p in predictions)
    avg_strength = total_strength / len(predictions)
    print(f"\nAverage Team Strength: {avg_strength:.1f}/100")
    
    # Display analysis
    if avg_strength >= 90:
        print("Analysis: Your predictions are very strong contenders!")
    elif avg_strength >= 80:
        print("Analysis: Your predictions are competitive teams!")
    else:
        print("Analysis: Your predictions are solid picks!")


def compare_countries():
    """Compare two countries side by side."""
    print("\n" + "=" * 60)
    print("COMPARE TWO COUNTRIES")
    print("=" * 60)
    
    selected_countries = []
    comparison_count = 0
    max_comparisons = 2
    
    while True:
        if comparison_count >= max_comparisons:
            break  # BREAK statement - exit when both countries selected
        
        print(f"\nSelect Country {comparison_count + 1}:")
        print("-" * 40)
        
        for rank in range(1, 11):
            country = TOP_10_COUNTRIES[str(rank)]
            print(f"  {rank}. {country['name']}")
        
        # Input validation loop
        while True:
            choice = input(f"\nEnter choice (1-10) or 'back' to return: ").strip()
            
            if choice.lower() == "back":
                return  # RETURN - exit comparison function
            elif choice in TOP_10_COUNTRIES:
                selected_countries.append(choice)
                break  # BREAK statement - valid input received
            else:
                print("Invalid choice. Please enter a number between 1 and 10.")
                continue  # CONTINUE statement - retry input
        
        comparison_count += 1
    
    # Display comparison
    if len(selected_countries) == 2:
        country1_data = TOP_10_COUNTRIES[selected_countries[0]]
        country2_data = TOP_10_COUNTRIES[selected_countries[1]]
        
        print("\n" + "=" * 60)
        print("COMPARISON RESULTS")
        print("=" * 60)
        
        # PASS statement - placeholder for future enhancement
        if False:
            pass  # Placeholder for additional comparison metrics
        
        print(f"\n{'Metric':<20} {country1_data['name']:<15} {country2_data['name']:<15}")
        print("-" * 60)
        print(f"{'Strength Rating':<20} {country1_data['strength']:<15} {country2_data['strength']:<15}")
        print(f"{'Previous Wins':<20} {country1_data['wins']:<15} {country2_data['wins']:<15}")
        print(f"{'Finals Appearances':<20} {country1_data['finals']:<15} {country2_data['finals']:<15}")
        print(f"{'Recent Form':<20} {country1_data['recent_form']:<15} {country2_data['recent_form']:<15}")
        
        # Determine winner
        if country1_data['strength'] > country2_data['strength']:
            print(f"\n➤ {country1_data['name']} appears to be the stronger contender!")
        elif country2_data['strength'] > country1_data['strength']:
            print(f"\n➤ {country2_data['name']} appears to be the stronger contender!")
        else:
            print("\n➤ Both teams are equally matched!")


def ranking_analysis():
    """Analyze rankings and provide insights."""
    print("\n" + "=" * 60)
    print("RANKING ANALYSIS & INSIGHTS")
    print("=" * 60)
    
    # Tier 1 - Top Contenders
    tier_1 = []
    tier_2 = []
    tier_3 = []
    
    # Categorize by strength
    for rank, country in TOP_10_COUNTRIES.items():
        strength = country['strength']
        
        if strength >= 90:
            tier_1.append(country['name'])
        elif strength >= 85:
            tier_2.append(country['name'])
        else:
            tier_3.append(country['name'])
    
    print("\n🏆 TIER 1 - CHAMPIONSHIP CONTENDERS (90+)")
    print("-" * 40)
    for idx, country_name in enumerate(tier_1, 1):
        print(f"  {idx}. {country_name}")
    
    print("\n🥈 TIER 2 - STRONG COMPETITORS (85-89)")
    print("-" * 40)
    for idx, country_name in enumerate(tier_2, 1):
        print(f"  {idx}. {country_name}")
    
    print("\n🥉 TIER 3 - SOLID TEAMS (80-84)")
    print("-" * 40)
    for idx, country_name in enumerate(tier_3, 1):
        print(f"  {idx}. {country_name}")
    
    # Most successful historically
    print("\n📊 MOST SUCCESSFUL HISTORICALLY (Most Titles)")
    print("-" * 40)
    sorted_by_wins = sorted(
        TOP_10_COUNTRIES.items(),
        key=lambda x: x[1]['wins'],
        reverse=True
    )
    
    for idx, (rank, country) in enumerate(sorted_by_wins[:5], 1):
        print(f"  {idx}. {country['name']}: {country['wins']} titles")
    
    print("\n" + "=" * 60)


def main():
    """Main program loop."""
    print("\n" + "=" * 60)
    print("WELCOME TO FIFA WORLD CUP 2026 WINNER PREDICTOR")
    print("=" * 60)
    
    while True:
        display_menu()
        
        # Input validation loop
        while True:
            choice = input("Enter your choice (1-5): ").strip()
            
            if choice in ["1", "2", "3", "4", "5"]:
                break  # BREAK statement - valid input received
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
                continue  # CONTINUE statement - retry input
        
        if choice == "1":
            view_countries()
        elif choice == "2":
            predict_winner()
        elif choice == "3":
            compare_countries()
        elif choice == "4":
            ranking_analysis()
        elif choice == "5":
            print("\n" + "=" * 60)
            print("Thank you for using World Cup 2026 Winner Predictor!")
            print("Good luck to your predicted teams!")
            print("=" * 60 + "\n")
            break  # BREAK statement - exit main loop
    
    return 0


if __name__ == "__main__":
    main()
