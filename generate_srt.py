import json
import sys

def seconds_str_to_srt_time(seconds_str):
    total_secs = float(seconds_str[:-1])
    mins = total_secs // 60
    secs = int(total_secs % 60)
    msecs = ((total_secs % 60) - secs) * 100
    return '00:%02d:%02d,%02d' % (mins, secs, msecs)

def main():
    fname = sys.argv[1]
    with open(fname, 'r') as in_f:
        content = json.load(in_f)
        results = content['results']
        i = 1
        with open(fname.split('.')[0] + '.srt', 'w') as out_f:
            for res in results:
                for w in res['alternatives'][0]['words']:
                    out_f.write(str(i) + '\n')
                    out_f.write(seconds_str_to_srt_time(w['startTime']) + ' --> ' + seconds_str_to_srt_time(w['endTime']) + '\n')
                    print('writing', w['word'].encode('UTF-8') + '\n\n')
                    out_f.write(w['word'].encode('UTF-8') + '\n\n')
                    i += 1


if __name__ == '__main__':
    main()
