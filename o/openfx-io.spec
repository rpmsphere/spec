%undefine _debugsource_packages

%define oname Natron
%define openfx_snapshot e91b1f921ff49694be3062f5cf9e6e60e9f741f3
%define sp_snapshot bbc96a9ee77d663e179c4c1431f32b37a32b8c3a
%define tinydir_snapshot 60f09057d32b8f193cbebb5a38644ca686994ea3
%define supportext_snapshot dd8c5c7e2618673af6801e42bb97639de0f0b041

Summary:	OpenFX IO Natron
Name:		openfx-io
Version:	1.0.0
Release:	4.6
License:	BSD
Group:		Video
URL:		https://github.com/MrKepzie/openfx-io
# From git by tag https://github.com/MrKepzie/openfx-io
Source0:	%{name}-%{oname}-%{version}-release.tar.gz
# From git https://github.com/devernay/openfx/
Source1:	openfx-%{openfx_snapshot}.zip
# From git https://github.com/MrKepzie/SequenceParsing
Source2:	SequenceParsing-%{sp_snapshot}.zip
# From git https://github.com/MrKepzie/tinydir
Source3:	tinydir-%{tinydir_snapshot}.zip
# From git https://github.com/devernay/openfx-supportext
Source4:	openfx-supportext-%{supportext_snapshot}.zip
Patch0:		openfx-ofx-path.patch
Patch1:		openfx-ofx-flags.patch
BuildRequires:	git atlas python2
BuildRequires:	ffmpeg-devel
BuildRequires:	OpenImageIO-devel
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(IlmBase)
BuildRequires:	pkgconfig(OpenColorIO)
BuildRequires:	OpenEXR-devel

%description
A set of Readers/Writers plugins written using the OpenFX standard.

%prep
%setup -qn %{name}-%{oname}-%{version}-release

# Unpack external libraries from sub-projects
rm -rf openfx
unzip -q %{SOURCE1}
mv openfx-%{openfx_snapshot} openfx

rm -rf SupportExt
unzip -q %{SOURCE4}
mv openfx-supportext-%{supportext_snapshot} SupportExt

pushd IOSupport
rm -rf SequenceParsing
unzip -q %{SOURCE2}
mv SequenceParsing-%{sp_snapshot} SequenceParsing
pushd SequenceParsing
rm -rf tinydir
unzip -q %{SOURCE3}
mv tinydir-%{tinydir_snapshot} tinydir
popd
popd

%patch0 -p1
%patch1 -p1

sed -i 's|-m64|-std=gnu++11|' Makefile* */Makefile* */*/Makefile* */*/*/Makefile*
sed -i 's|PIX_FMT_RGB24|AV_PIX_FMT_RGB24|' FFmpeg/FFmpegHandler.cpp FFmpeg/WriteFFmpeg.cpp
sed -i -e 's|PixelFormat|AVPixelFormat|' -e 's|PIX_FMT_YUV420P|AV_PIX_FMT_YUV420P|' -e 's|AVFMT_RAWPICTURE|0x0020|' -e 's|CODEC_FLAG_GLOBAL_HEADER|AV_CODEC_FLAG_GLOBAL_HEADER|' -e '481,482d' FFmpeg/WriteFFmpeg.cpp
sed -i -e 's|CODEC_CAP_DELAY|AV_CODEC_CAP_DELAY|' -e 's|CODEC_CAP_DR1|AV_CODEC_CAP_DR1|' -e '276,277d' FFmpeg/FFmpegHandler.cpp

%build
make CONFIG=release

%install
mkdir -p %{buildroot}%{_libdir}/OFX/Plugins
cp -r IO/Linux-*-release/IO.ofx.bundle %{buildroot}%{_libdir}/OFX/Plugins/

%files
%dir %{_libdir}/OFX/Plugins/IO.ofx.bundle
%{_libdir}/OFX/Plugins/IO.ofx.bundle/*

%changelog
* Tue May 31 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.0
- Rebuilt for Fedora
* Sat Feb 06 2016 Denis Silakov <dsilakov@gmail.com> 1.0.0-3
- (f5bd92c) Rebuild with new OpenImageIO
