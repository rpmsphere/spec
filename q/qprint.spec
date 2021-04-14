Name:           qprint
License:        SUSE-Public-Domain
Group:          Productivity/Security
Summary:        A simple command-line en/decoding filter
Version:        1.0
Release:        20.1
Source:         http://ftp.debian.org/debian/pool/main/q/qprint/qprint_%{version}.dfsg.2.orig.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
QPRINT is a simple command-line filter which encodes and decodes
files in Quoted-Printable encoding as defined in RFC 1521. For
details on operation of the program, please consult the manual
page "qprint.1".

%prep
%setup -q -n qprint-%{version}.dfsg.2

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr --mandir=%_mandir
make

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT%_mandir/man1
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%_bindir/qprint
%_mandir/man1/qprint.1.gz

%changelog
* Sun Aug 05 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
* Thu Oct 28 2010 aj@suse.de
- Use RPM_OPT_FLAGS.
- Fix build.
* Fri Oct 22 2010 joop.boonen@opensuse.org
- Build version 1.0
