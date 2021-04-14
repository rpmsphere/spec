Summary: Classic Basic interpreter
Name: blassic
Version: 0.11.0
Release: 6.1
License: GPL
Group: Development/Languages
URL: http://blassic.net/
Source: http://blassic.net/bin/%{name}-%{version}.tgz
BuildRequires: gcc-c++
BuildRequires: svgalib-devel

%description
Blassic is a classic Basic interpreter. The line numbers are
mandatory, and it has PEEK & POKE. The main goal is to execute
programs written in old interpreters, but it can be used as a
scripting language.

%prep
%setup -q
sed -i '258s/ScreenMap::create/create/' graphics.cpp
sed -i '1i #include <cstring>' blassic.cpp cursor.cpp socket.cpp graphics.cpp graphics_impl.cpp memory.cpp program.cpp runnerline_instructions.cpp
sed -i '1i #include <cstdlib>' util.h
sed -i 's/typedef map/typedef std::map/' var.cpp
sed -i 's/swap/std::swap/' graphics_impl.h

%build
cp /usr/share/automake-*/config.guess .
./configure --prefix=/usr --enable-installed-examples --enable-svgalib
make

%install
rm -fR $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -fR $RPM_BUILD_ROOT

%files
%doc AUTHORS NEWS README THANKS TODO
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Sat Apr 02 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.11.0
- Rebuilt for Fedora
