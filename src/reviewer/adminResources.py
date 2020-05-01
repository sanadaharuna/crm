from import_export import resources

from .models import Reviewer


class ReviewerResource(resources.ModelResource):
    class Meta:
        model = Reviewer
        skip_unchanged = True
        report_skipped = False
        import_id_fields = (
            "fiscalyear",
            "committee",
            "researcher",
            "name",
            "affiliation",
            "is_awarded",
        )

