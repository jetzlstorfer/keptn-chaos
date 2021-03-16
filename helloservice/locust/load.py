from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    
    # @task
    # def index(self):
    #     self.client.get("/")

    @task
    def health(self):
        with self.client.get("/health") as response:
            if response.status_code == 404:
                response.success()

