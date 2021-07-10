Name:           compat-SFML16
Version:        1.6
Release:        8
Summary:        Simple and Fast Multimedia Library
# src/SFML/Audio/stb_vorbis/stb_vorbis.{c,h} are Public Domain
License:        zlib and Public Domain
URL:            http://www.sfml-dev.org/
Source0:        http://downloads.sourceforge.net/sfml/SFML-%{version}-sdk-linux-64.tar.gz
Patch0:         SFML-1.6-gcc.patch
Patch1:         SFML-1.6-shared-libs.patch
Patch2:         SFML-1.6-cflags.patch
Patch3:         SFML-1.6-libpng15.patch
Patch4:         SFML-1.6-missing-includes.patch
BuildRequires:  freetype-devel
BuildRequires:  glew-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libsndfile-devel
BuildRequires:  SOIL-devel
BuildRequires:  libXrandr-devel
BuildRequires:  openal-devel

%description
SFML is a portable and easy to use multimedia API written in C++. You can see
it as a modern, object-oriented alternative to SDL.
SFML is composed of several packages to perfectly suit your needs. You can use
SFML as a minimal windowing system to interface with OpenGL, or as a
fully-featured multimedia library for building games or interactive programs.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n SFML-%{version}
%patch0 -p1 -b .gcc
%patch1 -p1 -b .shared-libs
%patch2 -p1 -b .cflags
%patch3 -p1 -b .libpng15
%patch4 -p1

# clean up bundled libs and prebuilt binaries
find . -depth \( -iname glew -o -iname glext -o -iname libjpeg -o -iname libpng -o -iname SOIL -o -iname zlib \) -exec rm -rf {} \;
rm -rf lib doc/SFML.chm
find samples/bin -type f -not -path \*datas\* -exec rm {} \;

# fix line endings
find . -type f -not \( -name \*.gif -o -name \*.jpg -o -name \*.png -o -name \*.ttf -o -name \*.wav \) -exec sed -i "s|\r||" {} \;

# fix permissions
find . -type f -exec chmod -x {} \;

%build
make %{?_smp_mflags} DEBUGFLAGS="$RPM_OPT_FLAGS"

%install
make install DESTDIR=$RPM_BUILD_ROOT DESTLIBDIR=$RPM_BUILD_ROOT%{_libdir} \
    DESTINCDIR=$RPM_BUILD_ROOT%{_includedir}/sfml1
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# Make parallel installable with 2.x, packages which still use 1.6 will
# need to have their build files patched to match
pushd $RPM_BUILD_ROOT%{_libdir}
for i in libsfml-*.so; do
    mv $i $(echo $i | sed 's/.so/-1.6.so/')
done
popd

%files
%doc license.txt readme-en.txt
%{_libdir}/*.so.*

%files devel
%doc doc/*
%{_includedir}/sfml1/
%{_libdir}/*-1.6.so

%changelog
* Sun Jul 04 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6
- Rebuilt for Fedora
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.6-7
- Rebuilt for GCC 5 C++11 ABI change
* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Mon Nov 18 2013 Hans de Goede <hdegoede@redhat.com> - 1.6-4
- Also rename the libsfml-foo.so symlinks to avoid conflicts with SFML 2.x
* Fri Nov 15 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 1.6-3
- Move headers to /usr/include/sfml1/ so SFML 2.x can be fixed to use
  default install locations as used also by its CMake script (#1023572).
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Sun May 26 2013 Hans de Goede <hdegoede@redhat.com> - 1.6-1
- Rename to compat-SFML16, the SFML will be taken by SFML 2.0 (rhbz#979801)
* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 1.6-9
- rebuild due to "jpeg8-ABI" feature drop
* Thu Dec 13 2012 Adam Jackson <ajax@redhat.com> - 1.6-8
- Rebuild for glew 1.9.0
* Fri Jul 27 2012 Julian Sikorski <belegdol@fedoraproject.org> - 1.6-7
- Rebuilt for glew-1.7
* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-5
- Rebuilt for c++ ABI breakage
* Fri Jan 13 2012 Julian Sikorski <belegdol@fedoraproject.org> - 1.6-4
- Fixed the License tag
* Thu Jan 12 2012 Julian Sikorski <belegdol@fedoraproject.org> - 1.6-3
- Use one patch and variables in place of sed to fix the makefile
- Fixed building with libpng-1.5 using a patch from Gentoo
- Updated the gcc patch for gcc-4.7
* Fri Dec 23 2011 Julian Sikorski <belegdol@fedoraproject.org> - 1.6-2
- s/libSOIL/SOIL
- Fixed the shared libs usage
* Wed Nov 30 2011 Julian Sikorski <belegdol@fedoraproject.org> - 1.6-1
- Initial RPM release based on Debian package
