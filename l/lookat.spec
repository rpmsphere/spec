Name:		lookat
Version:	2.0.1
Release:	1
Summary:	Lookat / bekijk is a program to view Un*x text files and man pages. 
Group:		Applications/Text
License:	GPLv2+	
URL:		https://www.wagemakers.be/english/programs/lookat
Source0:	lookat_bekijk-%{version}.tar.gz
BuildRequires:	gcc, ncurses-devel
Requires:	ncurses-libs	

%description
"lookat"  (or "bekijk" in the Dutch version) is a program to view Un*x text
files and manual pages.

Under DOS I used list.com to view text files. I didn't find such a program
under my favorite OS, GNU/Linux. The standard Un*x utilities ( more, less,
view ...) weren't userfriendly enough. For this reason I created "lookat".

%prep
%setup -q -n lookat_bekijk-%{version}
./configure --prefix=/usr --sysconfdir=/etc --mandir=/usr/share/man

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/*
%doc /usr/share/doc/lookat
%{_mandir}/man1/*.1.*
%config /etc/lookat.conf
%config /etc/lookat.conf.default

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.1
- Rebuilt for Fedora
