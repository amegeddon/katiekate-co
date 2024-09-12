from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from model_bakery import baker
import pytest
from store.models import Collection, Product

# Create your tests here. MUST FINISH REFACTORING - API_CLIENT etc - use model baker to create collections

@pytest.fixture
def create_collection(api_client):
    def do_create_collection(collection):
        return api_client.post('/store/collections/', collection)
    return do_create_collection


@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_anonymous_returns_401(self, create_collection):
        response = create_collection({'title': 'a'})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self, authenticate, create_collection):
        authenticate()

        response = create_collection({'title': 'a'})

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_returns_400(self, authenticate, create_collection):
        authenticate(is_staff=True)

        response = create_collection({'title': ''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None

    def test_if_data_is_valid_returns_201(self, authenticate, create_collection):
        authenticate(is_staff=True)

        response = create_collection({'title': 'a'})

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0
        
@pytest.mark.django_db
class TestListCollection:
    
    @pytest.fixture(autouse=True)  # is this setup method necessary or can the collection object simply be added to the main method?
    def setUp(self):
        # Create test collection data
        self.client = APIClient()
        
        Collection.objects.create(title='Test Collection')
    
    def test_list_collections(self):
        client = APIClient()
       
        response = client.get('/store/collections/')
       
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) > 0    
        
@pytest.mark.django_db
class TestDeleteCollection: 
    
     def test_delete_collection_as_admin_returns_204(self):
        collection = baker.make('Collection')
        client = APIClient()
        client.force_authenticate(user=User(is_staff =True)) 
       
        response = client.delete(f'/store/collections/{collection.id}/')
       
        assert response.status_code == status.HTTP_204_NO_CONTENT  
        
     def test_delete_collection_as_anonymous__returns_403(self):
        collection = baker.make('Collection')
        client = APIClient()
        client.force_authenticate(user={}) 
       
        response = client.delete(f'/store/collections/{collection.id}/')
       
        assert response.status_code == status.HTTP_403_FORBIDDEN
        
     def test_delete_collection_with_products_as_admin_returns_405(self):
        
        collection_with_products = baker.make('Collection', title='Collection with Products')
        baker.make('Product', title='Test Product', unit_price=10, inventory=5, collection=collection_with_products)
        client = APIClient()
        client.force_authenticate(user=User(is_staff =True)) 
       
        response = client.delete(f'/store/collections/{collection_with_products.id}/')
       
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert response.data['error'] == 'Collection cannot be deleted at this time because it is associated with one or more products'
        
@pytest.mark.django_db
class TestUpdateCollection: 
    
     def test_update_collection_as_admin_returns_200(self):
        collection = baker.make('Collection')
        client = APIClient()
        client.force_authenticate(user=User(is_staff =True))  
        
        response = client.put(f'/store/collections/{collection.id}/', {'title': 'Updated Title'})
        
        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == 'Updated Title'

     
     def test_update_collection_as_anonymous_returns_403(self):
        collection = baker.make('Collection')
        client = APIClient()
        client.force_authenticate(user={})  
        
        response = client.put(f'/store/collections/{collection.id}/', {'title': 'Updated Title'})
        
        assert response.status_code == status.HTTP_403_FORBIDDEN   
             
@pytest.mark.django_db
class TestRetrieveCollection:
    def test_if_collection_exists_returns_200(self, api_client):
        collection = baker.make(Collection)

        response = api_client.get(f'/store/collections/{collection.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': collection.id,
            'title': collection.title,
            'products_count': 0
        }


                  