from dataclasses import dataclass


@dataclass(frozen=True)
class Job:
    name: str
    attempts: int = 0


def retry(job: Job) -> Job:
    return Job(name=job.name, attempts=job.attempts + 1)


if __name__ == "__main__":
    print(retry(Job("example")))

