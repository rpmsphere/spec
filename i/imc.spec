Name: imc
Summary: The Image Compiler
Version: 4.3
Release: 8.1
Group: Applications/Multimedia
License: GPLv2
URL: http://users.skynet.be/Peter.Verthez/projects/imc/
Source0: http://www.peterverthez.net/projects/imc/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: perl-GD
BuildRequires: perl-CGI
BuildArch: noarch
Requires: perl-GD

%description
I wrote a Perl program at home that would just need an input of graphical
commands to generate the GIF file. That was gifc, which was later on released
to the world (on August 30, 1998). However, when Unisys was enforcing its GIF
patent, the Internet was turning away from GIF images (remember the "Burn all
GIFs" day at November 5, 1999). Therefore, from release 4.0 on, my program did
not generate GIF images anymore, but PNG images. It was therefore renamed to
imc, in anticipation of supporting more image types in the future.  In fact,
starting from release 4.1, JPEG output is also supported. Later, the patent
storm cleared, and now imc again supports GIF images (starting from release 4.3).

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install
sed -i 's|#! /bin|#! /usr/bin|' %{buildroot}%{_bindir}/*

%files
%doc README NEWS COPYING ChangeLog AUTHORS THANKS Todo
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Mon Oct 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 4.3
- Rebuilt for Fedora
