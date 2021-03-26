Summary: Display wallpaper clocks from vladstudio.com
Name: wallclock
Version: 0.8
Release: 3.1
BuildArch: noarch
License: GPLv3
Group: User Interface/Desktops
Source0: http://wallclock.googlecode.com/files/%{name}-%{version}.zip
URL: http://code.google.com/p/wallclock/
Requires: gnome-session, ImageMagick

%description
wallclock is a Bash script which will display wallpaper clocks on computers
running Linux with the GNOME desktop environment. It is designed to be run
using the cron job scheduler, so users must add a line to their crontab file
to run the script. Setting up the wallclock script does not take long and
detailed step-by-step instructions are available so that users unfamiliar
with editing their crontab file can easily set the script up.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -Dm 0755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Mar 21 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8
- Rebuild for Fedora
