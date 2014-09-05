#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nx.constants import *


ENUM_MTYPES = [
    [0 , "File"],
    [1 , "Virtual"],
]

ENUM_CTYPES = [
    [TEXT,  "Text"],
    [VIDEO, "Video"],
    [AUDIO, "Audio"],
    [IMAGE, "Image"]
]


BASE_META_SET = [

# NAMESPACE  TAG         EDITABLE SEARCHABLE CLASS   DEFAULT   SETTINGS

("o",  "id_object",              0, 0, INTEGER,    0,         False),
("o",  "ctime",                  0, 0, DATETIME,   0,         False),
("o",  "mtime",                  0, 0, DATETIME,   0,         False),

("a",  "media_type",             0, 0, SELECT,     0,         ENUM_MTYPES),        # FILE / VIRTUAL
("a",  "content_type",           0, 0, SELECT,     0,         ENUM_CTYPES),        # VIDEO / AUDIO /  IMAGE / TEXT 
("a",  "id_folder",              1, 0, INTEGER,    0,         False),     
("a",  "origin",                 0, 0, TEXT,       "Unknown", False),              # "Import", "Acquisition", "Library", "Ingest", "Edit", "Playout 1" ....
("a",  "status",                 0, 0, INTEGER,    0,         False),              # OFFLINE, ONLINE, CREATING, TRASHED, ARCHIVED
("a",  "version_of",             0, 0, INTEGER,    0,         False),

("e",  "start",                  1, 0, DATETIME,   0,         False),
("e",  "stop",                   1, 0, DATETIME,   0,         False),
("e",  "id_channel",             1, 0, INTEGER,    0,         False),
("e",  "id_magic",               0, 0, INTEGER,    0,         False),

("b",  "bin_type",               0, 0, INTEGER,    0,         False),

("i",  "id_asset",               0, 0, INTEGER,    0,         False),
("i",  "id_bin",                 0, 0, INTEGER,    0,         False),
("i",  "position",               0, 0, INTEGER,    0,         False),              # Order of the item within the bin

("u",  "login",                  0, 0, TEXT,       0,         False),              # Order of the item within the bin
("u",  "password",               0, 0, TEXT,       0,         False),              # Order of the item within the bin


#
# Virtual tags 
#

("v", "rundown_symbol",          0, 0, -1,         0,         False),              # Primary symbol in rundown view (folder color for items, star for event promo)
("v", "rundown_status",          0, 0, -1,         0,         False),              # OFFLINE, READY etc
("v", "rundown_broadcast",       0, 0, -1,         0,         False),              # Scheduled start time of block/item
("v", "rundown_scheduled",       0, 0, -1,         0,         False),              # Real computed start time of the item
("E", "run_mode",                0, 0, INTEGER,    0,         False),              # AUTO / MANUAL / SOFT AUTO / HARD AUTO

#
# Base metadata
#

("A",  "id_storage",             0, 0, INTEGER,     0,        False),
("A",  "path",                   1, 1, TEXT,        "",       False),
("A",  "article",                1, 1, BLOB,        "",       {"syntax" : "md"}),
("A",  "subclips",               0, 0, REGIONS,     "[]",     False),
("A",  "meta_probed",            0, 0, BOOLEAN,     0,        False),              # If true, meta_probes would not overwrite non-technical metadata during update

("AI", "mark_in",                1, 0, TIMECODE,    0,        False),
("AI", "mark_out",               1, 0, TIMECODE,    0,        False),

("AIEB",  "title",               1, 1, TEXT,        "",       False),              # dc.title.main - The title most commonly associated with the resource. Where no TYPE is specified, main is assumed. A main title is required for every resource.
("AIEB",  "title/subtitle",      1, 1, TEXT,        "",       False),              # dc.title.subtitle - Ancillary title information for the resource. A main title is required before subtitle(s) may be used.
("AIEB",  "title/alternate",     1, 1, TEXT,        "",       False),              # dc.title.alternate - Where a resource is known by more than one name, or where it has a formal name and a vernacular name, the alternate or vernacular name may be recorded here. A main title recording the full and formal name is required before an alternate title may be given.
("AIEB",  "title/series",        1, 1, CS_SELECT,   "",       "series"),           # dc.title.series - Where the resource is part of a series (CBA Research Reports, Star Trek, or whatever), the series name may be given here."
("AIEB",  "title/original",      1, 1, TEXT,        "",       False),              # ebucore.title.original
("AIEB",  "description",         1, 1, BLOB,        "",       {"syntax" : "md"}),
("AIEB",  "description/original",1, 1, BLOB,        "",       {"syntax" : "md"}),
("AIEB",  "promoted",            1, 0, BOOLEAN,     0,        False),              # Asset "promotion". It"s hit, important, favourite,....

("AIEB",  "series/season",       1, 0, INTEGER,     0,        False),
("AIEB",  "series/episode",      1, 0, INTEGER,     0,        False),
#
# Asset descriptive metadata
#

("m",  "language",               1, 0, CS_SELECT,   "en-US",  "languages"),
("m",  "date",                   1, 0, DATETIME,    0,        False),
("m",  "subject",                1, 1, BLOB,        "",       False),              # Keywords
("m",  "rights",                 1, 1, BLOB,        "",       False),
("m",  "version",                1, 1, TEXT,        "",       False),

("m",  "source",                 0, 1, TEXT,        "",       False),              # Youtube, Vimeo, PirateBay....
("m",  "source/url",             0, 1, TEXT,        "",       False),              # youtube url, torrent magnet link....

("m",  "format",                 1, 1, CS_SELECT,   "",       "formats"),          # documentary / featrure / clip / sport event / ....
("m",  "genre",                  1, 1, CS_SELECT,   "",       "genres"),           # horror / football / punk rock

("m",  "identifier/main",        1, 1, TEXT,        "",       False),              # Primary Content ID (IDEC, GUID...)
("m",  "identifier/youtube",     0, 1, TEXT,        "",       False),              # Youtube ID if exists
("m",  "identifier/vimeo",       0, 1, TEXT,        "",       False),              # Vimeo ID if exists
("m",  "identifier/imdb",        1, 1, TEXT,        "",       False),              # IMDB ID for movies

("m",  "role/director",          1, 1, TEXT,        "",       False),              # ebu_RoleCode 20.16
("m",  "role/composer",          1, 1, TEXT,        "",       False),              # ebu_RoleCode 17.1.7 (music) 
("m",  "role/performer",         1, 1, TEXT,        "",       False),              # ebu_RoleCode 17.2   (music) (A.K.A Artist)


("m",  "album",                  1, 1, TEXT,        "",       False),
("m",  "album/track",            1, 0, INTEGER,     0,        False),
("m",  "album/disc",             1, 0, INTEGER,     0,        False),

("m",  "contains/cg_text",       1, 0, BOOLEAN,     0,        False),              # TODO: Create ENUMS for contains/* (full frontal etc.)
("m",  "contains/nudity",        1, 0, BOOLEAN,     0,        False),
("m",  "contains/violence",      1, 0, BOOLEAN,     0,        False),

#
# "FMT" name space:
# Asset technical metadata.
# Should be reset on media file change
#

("fmt", "duration",              0, 0, TIMECODE,    0 ,       False),              # Clip duration. From ffprobe/format/duration. if fails, taken from streams[0]/duration
("fmt", "file/mtime",            0, 0, DATETIME,    0 ,       False),              # Timestamp of file last modification
("fmt", "file/size",             0, 0, INTEGER,     0 ,       False),              # File size in bytes
("fmt", "file/format",           0, 0, TEXT,        "",       False),              # Container format name. from ffprobe/format/format_name
("fmt", "video/width",           0, 0, INTEGER,     0 ,       False),              # Video frame / image width (pixels)
("fmt", "video/height",          0, 0, INTEGER,     0 ,       False),              # Video frame / image height (pixels)
("fmt", "video/fps",             0, 0, FRACTION,    "",       False),
("fmt", "video/pixel_format",    0, 0, TEXT,        "",       False),
("fmt", "video/aspect_ratio",    0, 0, FRACTION,    "",       False),
("fmt", "video/codec",           0, 0, TEXT,        "",       False),
("fmt", "audio/codec",           0, 0, TEXT,        "",       False),

#
# "QC" name space:
# These metadata hold results of automated asset quality control process
# Should be reset on media file change
#

("qc", "qc/state",               1, 0, ENUM,        0,        {0 : "New", 3 : "Rejected", 4 : "Approved"}),   # 1 and 2 are reserved for Auto QC failed and passed states
("qc", "qc/report",              1, 0, BLOB,        "",       False),              # Holds error report from QC Pass and/or rejection/approval message from QC humanoid
("qc", "audio/bpm",              0, 0, NUMERIC,     0,        False),              # Music BPM
("qc", "audio/r128/i",           0, 0, NUMERIC,     0,        False),              # Integrated loudness (LUFS)
("qc", "audio/r128/t",           0, 0, NUMERIC,     0,        False),              # Integrated loudness threshold (LUFS)
("qc", "audio/r128/lra",         0, 0, NUMERIC,     0,        False),              # LRA (LU)
("qc", "audio/r128/lra/t",       0, 0, NUMERIC,     0,        False),              # Loudness range threshold (LUFS)
("qc", "audio/r128/lra/l",       0, 0, NUMERIC,     0,        False),              # LRA Low (LUFS)
("qc", "audio/r128/lra/r",       0, 0, NUMERIC,     0,        False),              # LRA High (LUFS)
("qc", "audio/silence",          0, 0, REGIONS,     "[]",     False),              # Areas with silent audio
("qc", "audio/clipping",         0, 0, REGIONS,     "[]",     False),              # Audio clipping areas
("qc", "video/black",            0, 0, REGIONS,     "[]",     False),              # Areas where video is black-only
("qc", "video/static",           0, 0, REGIONS,     "[]",     False)               # Areas with static image
]





META_ALIASES = [

### Tohle se musi syncnout s tema tagama nahore (le bordel)

("id_object"            , "en-US", "Object ID",         "#"),
("media_type"           , "en-US", "Media type",        None),
("content_type"         , "en-US", "Content type",      ""),
("id_folder"            , "en-US", "Folder",            None),
("ctime"                , "en-US", "Created",           None),
("mtime"                , "en-US", "Modified",          None),
("origin"               , "en-US", "Origin",            None),
("version_of"           , "en-US", "Version of",        None),
("status"               , "en-US", "Status",            None),

("id_storage"           , "en-US", "Storage",           None),
("path"                 , "en-US", "Path",              None),
("state"                , "en-US", "Approval",          None),
("mark_in"              , "en-US", "Mark in",           None),
("mark_out"             , "en-US", "Mark out",          None),
("subclips"             , "en-US", "Subclips",          None),
("article"              , "en-US", "Article",           None),

("title"                , "en-US", "Title",             None),
("title/subtitle"       , "en-US", "Subtitle",          None),
("title/alternative"    , "en-US", "Alt. title",        None),
("title/series"         , "en-US", "Series",            None),
("title/original"       , "en-US", "Orig. title",       None),
("description"          , "en-US", "Description",       None),
("description/original" , "en-US", "Orig. description", None),
("promoted"             , "en-US", "promoted",          ""),


("language"             , "en-US", "Language",          None),
("date"                 , "en-US", "Date",              None),
("subject"              , "en-US", "Keywords",          None),
("rights"               , "en-US", "Rights",            None),
("version"              , "en-US", "Version",           None),

("format"               , "en-US", "Format",            None),
("genre"                , "en-US", "Genre",             None),

("identifier/main"      , "en-US", "IDEC",              None),
("identifier/youtube"   , "en-US", "Youtube ID",        None),
("identifier/vimeo"     , "en-US", "Vimeo ID",          None),

("role/director"        , "en-US", "Director",          None),
("role/performer"       , "en-US", "Artist",            None),
("role/composer"        , "en-US", "Composer",          None),

("album"                , "en-US", "Album",             None),
("album/track"          , "en-US", "Track",             None),
("album/disc"           , "en-US", "Disc",              None),

("series/season"        , "en-US", "Season",            None),
("series/episode"       , "en-US", "Episode",           None),

### Odsud dal by to melo sedet

("rundown_symbol"       , "en-US", "Rundown symbol",                         ""),
("rundown_status"       , "en-US", "Status",                                 None),
("rundown_broadcast"    , "en-US", "Broadcast time",                         "Broadcast"),
("rundown_scheduled"    , "en-US", "Scheduled time",                         "Scheduled"),
("run_mode"             , "en-US", "Run mode",                               "Run"),

("file/format"          , "en-US", "File format",                            None),
("file/mtime"           , "en-US", "File changed",                           None),
("file/size"            , "en-US", "File size",                              None),
("duration"             , "en-US", "Duration",                               None),
("video/width"          , "en-US", "Width",                                  None),
("video/height"         , "en-US", "Height",                                 None),
("video/fps"            , "en-US", "Frame rate",                             "FPS"),
("video/pixel_format"   , "en-US", "Pixel format",                           None),
("video/aspect_ratio"   , "en-US", "Aspect ratio",                           "Aspect"),
("video/codec"          , "en-US", "Video codec",                            None),
("audio/codec"          , "en-US", "Audio codec",                            None),

("qc/state"             , "en-US", "QC State",                               "QC"),
("qc/report"            , "en-US", "QC Report",                              None),
("audio/bpm"            , "en-US", "BPM",                                    None),
("audio/r128/i"         , "en-US", "Integrated loudness (LUFS)",             "Loudness"),
("audio/r128/t"         , "en-US", "Integrated loudness threshold (LUFS)",   "ILT"),
("audio/r128/lra"       , "en-US", "LRA (LU)",                               "LRA"),
("audio/r128/lra/t"     , "en-US", "Loudness range threshold (LUFS)",        "LRT"),
("audio/r128/lra/l"     , "en-US", "LRA Low (LUFS)",                         "LRA-L"),
("audio/r128/lra/r"     , "en-US", "LRA High (LUFS)",                        "LRA-H"),
("audio/silence"        , "en-US", "Areas with silent audio",                "Silences"),
("audio/clipping"       , "en-US", "Audio clipping areas",                   "Clipping"),
("video/black"          , "en-US", "Areas where video is black-only",        "Blacks"),
("video/static"         , "en-US", "Areas with static image",                "Statics"),

]

