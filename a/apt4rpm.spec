Name:           apt4rpm
Summary:        Create an APT repository
Version:        0.69.3
Release:        6.1
Source:         %{name}-%{version}.tar.bz2
License:        GPL
BuildArch:      noarch
URL:            https://apt4rpm.sourceforge.net
Requires:       perl-XML-LibXML wget mktemp
BuildRequires:  perl bash
Group:          System Environment/Base
%define pkgdocdir       %{_defaultdocdir}/%{name}

%description
This application creates an Advanced Package Tool (APT) 
repository from rpm packages.

%prep
%setup -q

%build
./configure PERL=/usr/bin/perl \
  --prefix=%{_prefix} \
  --mandir=%{_mandir} \
  --datadir=%{_datadir} \
  --libdir=/usr/lib \
  --sysconfdir=%{_sysconfdir} \
  --enable-pkgdocdir=%{pkgdocdir}

make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%files
%config(noreplace) %{_sysconfdir}/apt/aptate.conf
%{_bindir}/*
%{_mandir}/man?/*
%{_datadir}/apt4rpm
/usr/lib/apt4rpm
%doc %{pkgdocdir}

%changelog
* Sun Sep 23 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.69.3
- Rebuilt for Fedora
* Tue Oct 28 2003 Richard Bos <rbos@users.sourceforge.net>
- Updated the group for suse
- check RPM_BUILD_ROOT for "/" during clean up
* Sat Aug 23 2003 R. Bos
- Moved the mktemp dependency from buildrequires to requires
- Added buildrequires docbook-toys jadetex for suse
* Wed Feb 26 2003 R. Bos
- Added mktemp dependency
* Tue Oct 11 2002 R. Bos
- Remove wget requirement (not in case rsync is used e.g.)
* Tue Oct 09 2002 R. Bos
- Add RedHat build requirement
* Tue Jun 04 2002 R. Corsepius
- Add %{_datadir}.
- Add mirrorlist.dtd.
* Tue May 28 2002 R. Corsepius
- Use auto*tools-based configuration
* Mon Feb 25 2002 R Bos
- Added docbook sgml formatted documentation
