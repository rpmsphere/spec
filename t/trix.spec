Name:           trix
Version:        0.94
Release:        16.1
URL:            http://trix.sourceforge.net/
License:        GPLv2+
Group:          Applications/Internet
Summary:        VypressChat(TM) compatible chat
Source:         %{name}-%{version}.tar.bz2
Patch0:         %{name}-%{version}-nonvoid.patch
BuildRequires:  libpng-devel
BuildRequires:  gcc-c++, zlib-devel, libjpeg-devel
BuildRequires:  qt3-devel
Requires:       qt3

%description
TriX is a serverless text chat, dedicated to using in small home or
office LAN's, that runs on Linux using Qt/X11 library. It is compatible
with Vypress Chat(TM) for Windows.

%prep
%setup -q
%patch0
sed -i '1i #include <unistd.h>' src/main.cpp

%build
export CPPFLAGS=-fpermissive
%configure --with-qt-dir=%{_libdir}/qt-3.3 --with-qt-libraries=%{_libdir}/qt-3.3/lib
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING ChangeLog README TODO INSTALL
%{_bindir}/trix
%{_datadir}/trix

%changelog
* Thu Mar 31 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.94
- Rebuilt for Fedora
* Thu Sep 11 2008 prusnak@suse.cz
- created package (v 0.94)
