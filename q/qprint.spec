Name:           qprint
License:        SUSE-Public-Domain
Group:          Productivity/Security
Summary:        A simple command-line en/decoding filter
Version:        1.1
Release:        1
Source:         https://ftp.debian.org/debian/pool/main/q/qprint/qprint_%{version}.dfsg.2.orig.tar.gz

%description
QPRINT is a simple command-line filter which encodes and decodes
files in Quoted-Printable encoding as defined in RFC 1521. For
details on operation of the program, please consult the manual
page "qprint.1".

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr --mandir=%_mandir
make

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT%_mandir/man1
make install DESTDIR=$RPM_BUILD_ROOT

%files
%_bindir/qprint
%_mandir/man1/qprint.1.gz

%changelog
* Sun Sep 25 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuilt for Fedora
* Thu Oct 28 2010 aj@suse.de
- Use RPM_OPT_FLAGS.
- Fix build.
* Fri Oct 22 2010 joop.boonen@opensuse.org
- Build version 1.0
