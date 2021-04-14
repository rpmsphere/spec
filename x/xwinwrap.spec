%undefine _debugsource_packages

Name:       xwinwrap 
Version:    0.9
Release:    1
Summary:    Xwinwrap and coolbg for animated desktop background
Group:      User Interface/Desktops
License:    GPL
URL:        https://github.com/Aaahh/xwinwrap
Source0:    %{name}-master.zip
BuildRequires:  gcc-c++ libX11-devel bzip2 libXext-devel libXrender-devel

%description
xwinwrap is a utility, written by David Reveman/Novell, that will make
cool things happen on your desktop. You can run your screensavers, play
movies etc and it will look as if they are part of your background.
Original source - https://launchpad.net/xwinwrap

%prep
%setup -q -n %{name}-master

%build
gcc -Wall -Wstrict-prototypes \
             -Wmissing-prototypes \
             -Wmissing-declarations \
             -Wredundant-decls \
             -lX11 -lXext -lXrender xwinwrap.c -o xwinwrap

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README.md
%{_bindir}/*

%changelog
* Wed Dec 11 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9
- Rebuilt for Fedora
* Fri Mar 5 2010 - Malcolm Lewis <coyoteuser@gmail.com> - 090215
- Initial build of shantz-xwinwrap version
