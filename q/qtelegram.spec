%define snapshot_date 20150603

Name:		qtelegram
Version:	1.0.0.%{snapshot_date}
Release:	1
Summary:	A Qt asynchronous library to be used as Telegram client
Group:		Development/Other
License:	GPLv3
URL:		https://launchpad.net/libqtelegram
# bzr branch lp:libqtelegram
# tar cjf libqtelegram-%{snapshot_date}.tar.bz2 libqtelegram
Source0:	libqtelegram-%{snapshot_date}.tar.bz2
BuildRequires:	cmake
BuildRequires:	pkgconfig(libmediainfo)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Multimedia)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(thumbnailer)

%description
It was based originally on telegram-cli code (https://github.com/vysheng/tg),
but it's now completely different. Now works using signal-slot mechanism
and has an external easy to use API for client applications to interact to.

%package	devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description	devel
Development files for %{name}.

%prep
%setup -q -n lib%{name}

%build
%{cmake} -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} .
make

%install
%make_install
mkdir -p %{buildroot}%{_libdir}
mv %{buildroot}/usr/**Unknown**/Telegram %{buildroot}%{_libdir}

%files
%doc README
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/Telegram
%{_libdir}/*.so

%changelog
* Wed Jun 03 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.0.20150603
- Rebuilt for Fedora
* Sat Feb 21 2015 sander85 <sander85> 1.0.0-20150221.1.mga5
+ Revision: 816248
- New release: 20150221
* Wed Jan 14 2015 sander85 <sander85> 1.0.0-20150113.2.mga5
+ Revision: 810661
- Fix major version
* Wed Jan 14 2015 sander85 <sander85> 1.0.0-20150113.1.mga5
+ Revision: 810634
- imported package libqtelegram
