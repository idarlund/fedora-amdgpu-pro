# pulls release info from versions file

. ./versions

#

echo "making final tarball"
cd ./debs/extract
tar -czvf ../../../../../amdocl-legacy-"$major"."$fedora".i686.tar.gz .


