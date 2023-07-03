Summary: The CRT screen quality testing utility
Name: screentest
Version: 2.0
Release: 5.1
License: GPLv2
Group: System/X11
Source: https://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz
URL: https://sourceforge.net/projects/%{name}/
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(libglade-2.0)

%description
Screentest is a simple program which displays various patterns
(colors, circles, grids, text) on your screen in order to allow you
to evaluate the quality of your CRT/LCD monitor (sharpness, linearity, etc).

%prep
%setup -q

%build
export LDFLAGS="-lgmodule-2.0"
%configure
make

%install
%make_install
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/%{name}
%{_datadir}/%{name}/%{name}.glade
%dir %{_datadir}/%{name}/

%changelog
* Sun Feb 22 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0
- Rebuilt for Fedora
* Fri Jul 25 2014 Denis Silakov <denis.silakov@rosalab.ru> 2.0-4
+ Revision: dac09e7
- MassBuild#464: Increase release tag


