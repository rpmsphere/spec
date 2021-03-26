Summary: An application for building user interfaces for set-top boxes
Name: eboxy
Version: 0.4.1
Release: 1
License: GPLv2
Group: Applications/Multimedia
URL: http://eboxy.sourceforge.net/
Source0: http://eboxy.sourceforge.net/eboxy-%{version}%{?prever:-%{prever}}.tar.bz2
Source1: http://www.bluelightning.org/ebox/files/eboxy/eboxskin-20040526.tar.gz
Patch0: cpp.patch
BuildRequires: gcc-c++, zip, zlib-devel, desktop-file-utils
BuildRequires: autoconf SDL-devel > 1.2.0 libxml2-devel > 2.4.19
BuildRequires: SDL_gui-devel, SDL_mixer-devel, SDL_ttf-devel
BuildRequires: SDL_image-devel, lirc-devel
#BuildRequires: flex <= 2.5.4a
BuildRequires: compat-flex

%package devel
Summary: Development files for eboxy

%description devel
Development files for eboxy.

%description
eboxy is an application for building user interfaces for set-top boxes,
suitable for use on a TV. It reads an XML file describing a simple GUI
consisting of pages, images, labels, listboxes and buttons, and creates the
GUI on the screen.
I wrote this software for my eBox project (a movie/audio playing home
entertainment PC), so I could access its various functions from the comfort
of the couch using a remote. The eBox project is as much about helping others
build similar systems as it is getting a decent entertainment system for
myself, so for detailed information on the eBox and how you can set up such
a system using Linux, check out the eBox website:
http://www.bluelightning.org/ebox

%prep
%setup -q -n %{name}-%{version}%{?prever:-%{prever}}
%patch0 -p1 -b .cpp
sed -i 's|FlexLexer.h|flex-2.5.4a/FlexLexer.h|' eboxy/script_flex.cpp eboxy/script.h
sed -i '1i #include <cstdio>' eboxy/script_flex.cpp eboxy/interfacemanager.cpp

%build
autoconf
export CFLAGS="%{optflags} -fPIC"
%configure \
%if %{with compat_flex}
           --with-extra-includes=%{_includedir}/flex-2.5.4a \
           --with-extra-libs=%{_libdir}/flex-2.5.4a
%endif

grep -rl lxml2 . | xargs sed -i -e's,-lxml2,-lxml2 -lpthread,g' 
make


%install
%{__rm} -rf %{buildroot}
%makeinstall

# Create a desktop entry
%{__cat} << EOF > %{name}.desktop
[Desktop Entry]
Name=eBoxy
Name[zh_TW]=數位機上盒
Comment=an application for building user interfaces for set-top boxes.
Comment[zh_TW]=eBoxy 建立機上盒使用者介面
Icon=%{name}
Exec=%{name} %{_datadir}/%{name}/eboxskin/eboxy.xml
Terminal=false
Type=Application
Categories=Application;AudioVideo;
EOF

# Complete the modifications
%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install --vendor "" \
    --dir %{buildroot}%{_datadir}/applications  \
    --add-category Application                  \
    --add-category AudioVideo                   \
    %{name}.desktop

# Install the image used in the desktop entry
%{__install} -D -m 644 images/eboxy.png \
%{buildroot}%{_datadir}/pixmaps/%{name}.png

tar xzvf %{SOURCE1} -C %{buildroot}%{_datadir}/%{name}

%clean
%{__rm} -rf %{buildroot}

%files
# The help is actually in %{_docdir}/%{name} in order to be accessible directly
#doc LICENSE.txt README.txt help
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/*

%files devel
%{_libdir}/%{name}/plugins/generic/*.la
%{_libdir}/libeboxyplugin.a
%{_includedir}/%{name}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.1
- Rebuild for Fedora
* Sat Dec 18 2008 Paulo Roma <http://orion.lcg.ufrj.br/~roma> 0.4.1-3
- Recreated gcc.patch for gcc 4.3
- Introduced compat_flex, because the test Fedora < 7 does not work
  for fc10.
* Sun Nov 18 2007 Paulo Roma <http://orion.lcg.ufrj.br/~roma> 0.4.1-2
- Rebuilt for Fedora 8.
- Fixed BRs and using compat-flex.
* Wed Apr  18 2007 Paulo Roma <http://orion.lcg.ufrj.br/~roma> 0.4.1-1
- Patched for compiling in gcc 4.1
* Thu Aug  18 2004 Paulo Roma <http://orion.lcg.ufrj.br/~roma> 0.4.1-1
- Initial RPM release.
