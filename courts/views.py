from django.shortcuts import get_object_or_404, redirect, render

from members.models import Member
from .models import Court


def courts(request):
    courts = Court.objects.all()
    all_members = Member.objects.filter(court__isnull=True)
    return render(
        request, "all_courts.html", {"courts": courts, "all_members": all_members}
    )

from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Court
from members.models import Member

def reserve_member(request, court_id, member_type):
    court = get_object_or_404(Court, id=court_id)

    # Fetch the selected member from the POST request
    member_id = request.POST.get(member_type)

    try:
        # Get the member object
        member = Member.objects.get(id=member_id)
    except Member.DoesNotExist:
        return HttpResponse(f"Member {member_id} not found.", status=404)

    # Check if this member is already assigned to another court
    if member.court:
        return HttpResponse(f"Member {member.firstname} {member.lastname} is already assigned to a court.", status=400)

    # Assign the court to the member
    member.court = court
    member.save()

    # Check if both members are assigned, and mark the court as occupied
    if court.members.count() == 2:
        court.is_occupied = True
        court.save()

    return redirect("/courts/")


def reserve(request, id):
    if request.method == "POST":
        court = get_object_or_404(Court, id=id)

        # Extract member names from the POST request
        member1 = request.POST.get("member1")
        member2 = request.POST.get("member2")
        print(f"reserving for members:{member1}, {member2}")
        # Update court information
        court.is_occupied = True
        # catch this court by member1 and member2

        member1_obj = Member.objects.get(id=member1)

        member2_obj = Member.objects.get(id=member2)

        member1_obj.court = court
        member2_obj.court = court
        member1_obj.save()
        member2_obj.save()
        court.save()

    return redirect("/courts/")


def unreserve(request, id):
    court = get_object_or_404(Court, id=id)
    # Check if the court is occupied
    if court.is_occupied:
        # Set court to not occupied
        court.is_occupied = False
        court.time_of_occupation = None  # Reset the time if needed
        court.save()
        # Clear the court for all members
        court.members.all().update(court=None)

    return redirect("/courts/")
