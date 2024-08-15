def company_name_processor(request):
    # Example test data
    test_data = [
        {
            'company': 'Test Company, UAB',
            'user': 'Vardas Pavardė'
            
        }
    ]
    
    # Extract values from the test data
    company_name = test_data[0]['company']
    user = test_data[0]['user']
    
    return {
        'company_name': company_name,
        'user': user
    }
