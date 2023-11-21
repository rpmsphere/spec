Name: transparency
Version: 2.9.1
Release: 1
License: GPLV2
Summary: Transparent applications suite
Group: User Interface/X
Source: %{name}-%{version}.tar.gz
BuildRequires: qt5-qtx11extras-devel

%description
transparent applications suite:
- transparent clock;
- transparent calendar;
- transparent cpu load meter;
- transparent memory load meter;
- transparent disk usage meter;
- transparent network load meter;
- transparent temperature meter.
- transparent pictures display.

%prep
%setup -q
sed -i '48i #include <QPainterPath>' calendar/CalendarWidget.cpp
sed -i '43i #include <QPainterPath>' clock/ClockWidget.cpp
sed -i '31i #include <array>' calendar/CalendarEventModel.h

%build
%define prefix /usr
cmake -DCMAKE_INSTALL_PREFIX=%{prefix} -DUSE_QT5=1 .
make -j4

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING INSTALL
%{prefix}/bin/transparency
%{prefix}/bin/transparency-settings
%{prefix}/bin/transparent-clock
%{prefix}/bin/transparent-calendar
%{prefix}/bin/transparent-pictures

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 2.9.1
- Rebuilt for Fedora
