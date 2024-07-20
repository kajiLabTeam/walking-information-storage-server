CREATE DATABASE indoor_location_estimation;

\c indoor_location_estimation;

CREATE TABLE pedestrians (
    id VARCHAR(26) PRIMARY KEY,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP WITH TIME ZONE
);

CREATE TABLE floor_maps (
    id VARCHAR(26) PRIMARY KEY,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE,
    deleted_at TIMESTAMP WITH TIME ZONE
);

CREATE TABLE floor_map_images (
    id VARCHAR(26) PRIMARY KEY,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE,
    deleted_at TIMESTAMP WITH TIME ZONE,
    floor_map_id VARCHAR(26) REFERENCES floor_maps(id)
);

CREATE TABLE trajectories (
    id VARCHAR(26) PRIMARY KEY,
    is_walking BOOLEAN NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE,
    deleted_at TIMESTAMP WITH TIME ZONE,
    pedestrian_id VARCHAR(26) REFERENCES pedestrians(id),
    floor_map_id VARCHAR(26) REFERENCES floor_maps(id)
);

CREATE TABLE realtime (
    id VARCHAR(26) PRIMARY KEY,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE,
    deleted_at TIMESTAMP WITH TIME ZONE,
    trajectory_id VARCHAR(26) REFERENCES trajectories(id)
);

CREATE TABLE modified (
    id VARCHAR(26) PRIMARY KEY,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE,
    deleted_at TIMESTAMP WITH TIME ZONE,
    trajectory_id VARCHAR(26) REFERENCES trajectories(id)
);

CREATE TABLE realtime_walking_samples (
    id VARCHAR(26) PRIMARY KEY,
    step INT NOT NULL,
    angle_changed DECIMAL(5, 2) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    realtime_id VARCHAR(26) REFERENCES realtime(id)
);

CREATE TABLE modified_walking_samples (
    id VARCHAR(26) PRIMARY KEY,
    step INT NOT NULL,
    angle_changed DECIMAL(5, 2) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    walking_at TIMESTAMP WITH TIME ZONE,
    modified_id VARCHAR(26) REFERENCES modified(id)
);

CREATE TABLE realtime_coordinates (
    id VARCHAR(26) PRIMARY KEY,
    x DECIMAL(10, 2) NOT NULL,
    y DECIMAL(10, 2) NOT NULL,
    realtime_walking_sample_id VARCHAR(26) REFERENCES realtime_walking_samples(id)
);

CREATE TABLE modified_coordinates (
    id VARCHAR(26) PRIMARY KEY,
    x DECIMAL(10, 2) NOT NULL,
    y DECIMAL(10, 2) NOT NULL,
    modified_walking_sample_id VARCHAR(26) REFERENCES modified_walking_samples(id)
);

CREATE TABLE access_points (
    id VARCHAR(26) PRIMARY KEY,
    address VARCHAR(17) NOT NULL CHECK (
        address ~* '([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})'
    ) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE finger_prints (
    id VARCHAR(26) PRIMARY KEY,
    rssi DECIMAL(5, 2),
    access_point_id VARCHAR(26) REFERENCES access_points(id),
    realtime_walking_sample_id VARCHAR(26) REFERENCES realtime_walking_samples(id)
);

CREATE TABLE raw_data (
    id VARCHAR(26) PRIMARY KEY,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    realtime_walking_sample_id VARCHAR(26) REFERENCES realtime_walking_samples(id)
);

CREATE TABLE particles (
    id VARCHAR(26) PRIMARY KEY,
    x DECIMAL(10, 2) NOT NULL,
    y DECIMAL(10, 2) NOT NULL,
    weight DECIMAL(5, 2) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    realtime_walking_sample_id VARCHAR(26) REFERENCES realtime_walking_samples(id)
);
