from sqlalchemy.orm import Session

from schemas.jobs import JobCreate
from db.models.jobs import Job


def create_new_job(job: JobCreate, db: Session, owner_id: int):
    job_object = Job(**job.dict(), owner_id=owner_id)
    db.add(job_object)
    db.commit()
    db.refresh(job_object)
    return job_object


def retreive_job(id: int, db: Session):
    item = db.query(Job).filter(Job.id == id).one_or_none()
    return item


def list_jobs(db: Session):
    jobs_object = db.query(Job).filter(Job.is_active == True).all()
    return jobs_object


def update_job_by_id(id: int, job: JobCreate, db: Session, owner_id: int):
    existing_job = db.query(Job).filter(Job.id == id)

    if not existing_job.one_or_none():
        return 0

    # update dictionary with new key value of owner_id
    job.__dict__.update(owner_id=owner_id)
    existing_job.update(job.__dict__)

    db.commit()

    return 1
