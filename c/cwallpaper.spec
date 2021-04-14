Name: cwallpaper
Summary: A frontend for root wallpaper changers
Version: 0.3.2
#Version: 0.4.2
Release: 2.1
Group: User Interface
License: GPLv2+
URL: http://cwallpaper.sourceforge.net/
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  gtk2-devel
BuildRequires:  pango-devel

%description
CWallpaper is a frontend for various root wallpaper changing programs
such as fbsetbg, hsetroot, and others. It is written in GTK.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc README NEWS AUTHORS ChangeLog COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Thu Mar 05 2015 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuilt for Fedora
