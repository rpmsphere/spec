%undefine _debugsource_packages

Name:       charm
Version:        1.0
Release:        7.1
License:        GPL-2.0
Summary:        The cross-platform time tracker
URL:    https://github.com/KDAB/Charm
Group:  Productivity/Office/Organizers
Source: %{name}-%{version}.tar.bz2
BuildRequires:  libpng-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt4-devel
BuildRequires:  git
BuildRequires:  desktop-file-utils

%description
Charm is a program for OS X, Linux and Windows that helps to keep track of time.
It is built around two major ideas - tasks and events. Tasks are the things time
is spend on, repeatedly. For example, ironing laundry is a task. The laundry
done for two hours on last Tuesday is an event in that task. When doing laundry
multiple times, the events will be accumulated, and can later be printed in
activity reports or weekly time sheets. So in case laundry would be done for
three hours on Wednesday again, the activity report for the "Ironing Laundry"
task would list the event on tuesday, the event on wednesday and a total of
five hours.

%prep
%setup -q

%build
mkdir -pv build
pushd build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DLIB_INSTALL_DIR=%{_libdir} \
        ..
make %{?_smp_mflags}

%install
rm -f -r $RPM_BUILD_ROOT
pushd build
make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/charmtimetracker/
sed -i -e "44d" -e 's|Exec=Charm|Exec=charmtimetracker|' $RPM_BUILD_ROOT%{_datadir}/applications/Charm.desktop
echo "Categories=Qt;KDE;Utility;TimeUtility;" >> $RPM_BUILD_ROOT%{_datadir}/applications/Charm.desktop

%files
%doc ReadMe.txt License.txt
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/

%changelog
* Thu Mar 15 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
* Mon Feb 20 2012 i@marguerite.su
- initial package 1.0 from git
