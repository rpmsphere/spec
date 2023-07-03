%undefine _debugsource_packages
Name: scratch-plugins
%define real_name  ScratchPluginSrc
%define real_version 1.4.0Linux
Summary: A new programming language
Summary(ru.UTF-8): Программирование для детей на основе Logo
Version: 1.4
Release: 1
Group: Education
License: Artistic License
URL: https://scratch.mit.edu/
Patch: 0001-Fix-build-UnicodePlugin.patch
Requires: squeak-vm, libv4l
Source: %real_name%version.zip
%define installdir %_datadir/Scratch
%define squeakver 3.10-5
# Automatically added by buildreq on Tue Jan 19 2010
BuildRequires: pango-devel, libv4l-devel

%description
Scratch is a new programming language that makes it easy to create your own
interactive stories, animations, games, music, and art -- and share your
creations on the web.

Scratch is designed to help young people (ages 8 and up) develop 21st century
learning skills. As they create Scratch projects, young people learn important
mathematical and computational ideas, while also gaining a deeper understanding
of the process of design.

%prep
%setup -n %real_name%version
%patch -p1

%build
pushd ScratchPlugin/ScratchPlugin-linux
./build.sh
popd
pushd UnicodePlugin/UnicodePlugin-linux
./unixBuild.sh
popd
pushd CameraPlugin/CameraPlugin-linux
./build.sh
popd

%install
%__rm -rf %{buildroot}
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_datadir/Scratch
mkdir -p %buildroot%_libdir/squeak
mkdir -p %buildroot%_libdir/squeak/%squeakver
install -Dm644 ScratchPlugin/ScratchPlugin-linux/ScratchPlugin %buildroot%_libdir/squeak/%squeakver/
install -Dm644 UnicodePlugin/UnicodePlugin-linux/UnicodePlugin %buildroot%_libdir/squeak/%squeakver/
install -Dm644 CameraPlugin/CameraPlugin-linux/CameraPlugin %buildroot%_libdir/squeak/%squeakver/

%clean
%__rm -rf %{buildroot}

%files
%_libdir/squeak

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4
- Rebuilt for Fedora
* Thu Jan 28 2010 Anton A. Vinogradov <arc@altlinux.org> 1.4-alt0.3
- spec cleanup
* Wed Jan 27 2010 Anton A. Vinogradov <arc@altlinux.org> 1.4-alt0.2
- initial build for ALT Linux
