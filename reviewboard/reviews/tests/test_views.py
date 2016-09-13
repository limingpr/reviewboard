from reviewboard.reviews.models import Comment, GeneralComment, Review
    """Tests for views in reviewboard.reviews.views."""

        self.siteconfig.set('auth_require_sitewide_login', False)
        comment_text_1 = 'Comment text 1'
        comment_text_2 = 'Comment text 2'
        comment_text_3 = 'Comment text 3'
        comments = entry.comments['diff_comments']
    def test_review_detail_general_comment_ordering(self):
        """Testing review_detail and ordering of general comments on a review
        """
        comment_text_1 = 'Comment text 1'
        comment_text_2 = 'Comment text 2'
        comment_text_3 = 'Comment text 3'
        review_request = self.create_review_request(create_repository=True,
                                                    publish=True)
        # Create the users who will be commenting.
        user1 = User.objects.get(username='doc')
        user2 = User.objects.get(username='dopey')

        # Create the master review.
        main_review = self.create_review(review_request, user=user1)
        main_comment = self.create_general_comment(main_review,
                                                   text=comment_text_1)
        main_review.publish()

        # First reply
        reply1 = self.create_reply(
            main_review,
            user=user1,
            timestamp=(main_review.timestamp + timedelta(days=1)))
        self.create_general_comment(reply1, text=comment_text_2,
                                    reply_to=main_comment)

        # Second reply
        reply2 = self.create_reply(
            main_review,
            user=user2,
            timestamp=(main_review.timestamp + timedelta(days=2)))
        self.create_general_comment(reply2, text=comment_text_3,
                                    reply_to=main_comment)

        # Publish them out of order.
        reply2.publish()
        reply1.publish()

        # Make sure they published in the order expected.
        self.assertTrue(reply1.timestamp > reply2.timestamp)

        # Make sure they're looked up in the order expected.
        comments = list(GeneralComment.objects.filter(
            review__review_request=review_request))
        self.assertEqual(len(comments), 3)
        self.assertEqual(comments[0].text, comment_text_1)
        self.assertEqual(comments[1].text, comment_text_3)
        self.assertEqual(comments[2].text, comment_text_2)

        """Testing visibility of file attachments on review requests"""
        comment_text_1 = 'Comment text 1'
        comment_text_2 = 'Comment text 2'
        review_request = self.create_review_request()
        file1 = self.create_file_attachment(review_request, caption=caption_1)
        file2 = self.create_file_attachment(review_request, caption=caption_2,
                                            active=False)
        # Create a third file attachment on a draft.
        self.create_file_attachment(review_request, caption=caption_3,
                                    draft=True)
        comments = entry.comments['file_attachment_comments']
        """Testing visibility of screenshots on review requests"""
        comment_text_1 = 'Comment text 1'
        comment_text_2 = 'Comment text 2'
        review_request = self.create_review_request()
        screenshot1 = self.create_screenshot(review_request, caption=caption_1)
        screenshot2 = self.create_screenshot(review_request, caption=caption_2,
                                             active=False)
        # Add a third screenshot on a draft.
        self.create_screenshot(review_request, caption=caption_3, draft=True)
        comments = entry.comments['screenshot_comments']
        self.siteconfig.set('auth_require_sitewide_login', True)
            print('Error: %s' % self._get_context_var(response, 'error'))
            print('Error: %s' % self._get_context_var(response, 'error'))
        user = User.objects.get(username='doc')
        """Testing /diff/raw/ multiple Content-Disposition issue"""
        self.create_diffset(review_request=review_request, name='test, comma')
        content_disposition = response['Content-Disposition']
        filename = content_disposition[len('attachment; filename='):]
    def _get_context_var(self, response, varname):
        for context in response.context:
            if varname in context:
                return context[varname]

        return None
