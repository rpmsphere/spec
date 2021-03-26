%global debug_package %{nil}

Name:          xfractint
Version:       20.04p14
Release:       3.1
Summary:       A freeware fractal generator
Group:         Graphical Desktop/Applications/Educational
URL:           http://www.fractint.org/
Source:        http://www.fractint.org/ftp/current/linux/xfractint-%{version}.tar.gz
License:       Freeware
BuildRequires: glibc-devel
BuildRequires: ncurses-devel
BuildRequires: libX11-devel
BuildRequires: libXft-devel

%description
Fractint is a freeware fractal generator created for IBMPC's and compatible computers.
It is the most versatile and extensive fractal program available for any price.
The authors (of which I am not one), work very hard to keep it that way.
It has many great features and it is constantly being upgraded and improved by the Stone Soup team.
Keep this link as a reference to stay up-to-date with the latest developments.

%prep
%setup -q
sed -i 's|-lm|-lm -Wl,--allow-multiple-definition|' Makefile

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=%{buildroot}/usr install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc fractsrc.txt read.me
%{_bindir}/xfractint
%{_mandir}/man1/xfractint.*
%{_datadir}/%{name}

%changelog
* Fri Apr 21 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 20.04p14
- Rebuild for Fedora
* Tue Aug 26 2008 Tiziana Ferro <tiziana.ferro@email.it> 20.2.04-2mamba
- update system menu entry, vendor, distribution, mantainer
- added buildrequirements
* Wed Sep 21 2005 Silvan Calarco <silvan.calarco@qilinux.it> 0.2.04-1qilnx
- package created by autospec
