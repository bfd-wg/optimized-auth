import os

list_of_ietf_models =\
[ ["ietf-crypto-types", "draft-ietf-netconf-crypto-types", "34"],
  ["ietf-truststore", "draft-ietf-netconf-trust-anchors", "20"],
  ["ietf-keystore", "draft-ietf-netconf-keystore", "35"],
  ["ietf-tcp-common", "draft-ietf-netconf-tcp-client-server", "26"],
  ["ietf-tcp-client", "draft-ietf-netconf-tcp-client-server", "26"],
  ["ietf-tls-client", "draft-ietf-netconf-tls-client-server", "41"],
  ["ietf-tls-common", "draft-ietf-netconf-tls-client-server", "41"],
  ["ietf-tls-server", "draft-ietf-netconf-tls-client-server", "41"],
  ["ietf-http-client", "draft-ietf-netconf-http-client-server", "20"] ]


def fetch_and_extract(draft, module, version):
    print("Fetching file " + draft + " with version " + version)
    draft_version = draft + "-" + version
    print(draft_version)
    os.system('curl -sO https://www.ietf.org/archive/id/%s.txt' %draft_version)
    print("Extracting Module from " + draft_version)
    os.system('xym %s.txt' %draft_version)
    print("Moving module " + module + " to ../bin/imported-modules/")
    os.system('mv %s* ../bin/imported-modules/' %module)
    print("Cleaning up ...")
    os.system('rm %s.txt' %draft_version)

def fetch(module, path):
    file = path + module + ".yang.txt"
    print("Fetching file " + file)
    os.system('curl -sO http://%s' %file)
    model = module + ".yang"
    print("Moving module " + model + " to ../bin/imported-modules/")
    os.system("mv '%s'.txt ../bin/imported-modules/'%s'" %(model, model))

os.system("mkdir -p ../bin/imported-modules")

for list in list_of_ietf_models:
    module, draft, version = list
    print(module)
    fetch_and_extract(draft, module, version)

os.system('rm *.yang')
