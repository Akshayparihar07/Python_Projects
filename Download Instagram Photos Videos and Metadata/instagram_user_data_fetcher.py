import instaloader

loader = instaloader.Instaloader() # get instance

USER = input("Enter your Username: ")
PASSWORD = input("Enter your Password: ")  # Password is required only if you want to get the followers, else you can skip this step 

profile = instaloader.Profile.from_username(loader.context,USER)


def getMetadata():
	print(profile.full_name)
	print(profile.followees)
	print(profile.followers)
	print(profile.mediacount)
	print(profile.has_public_story)
	print(profile.igtvcount)
	print(profile.is_private)
	print(profile.biography)
	print(profile.profile_pic_url)
	print(profile.external_url)
	print(profile.is_business_account)
	print(profile.business_category_name)
	print(profile.biography_hashtags)
	print(profile.followed_by_viewer)
	print(profile.blocked_by_viewer)
	print(loader.check_profile_id(USER))

def downloadProfilepic(USER):
	profile.download_profile(USER,profile_pic_only=True)

def getFollowers(USER, PASSWORD):
	loader.login(USER, PASSWORD)
	followers = profile.get_followers()  # get followers list
	for follower in followers:
		print(follower)
	followees = profile.get_followees()  # get followees list
	for followee in followees:
		print(followee)

def downloadPosts(USER):
	posts_sorted_by_likes = sorted(profile.get_posts(), key=lambda post: post.likes, reverse=True) # sort posts according to likes count
	for post in posts_sorted_by_likes:
    		loader.download_post(post, USER)
		
def downloadStories(USER, PASSWORD):
	loader.login(USER, PASSWORD)
	profile_id = loader.check_profile_id(input("Enter the Username of the Profile you want to get ID of: "))
	print(profile_id)
	loader.download_stories(userids = print(profile_id))

# EXECUTE ALL THE FUNCTIONS
getMetadata() # to get internal metadata 
downloadProfilepic(USER) # to download the profile picture
getFollowers(USER, PASSWORD) # to get the followers and followings
downloadPosts(USER)  # to download all the posts
downloadStories(USER, PASSWORD) #to download stories 
