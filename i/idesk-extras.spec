Name: idesk-extras
Version: 1.37
Release: 1
Summary: A collection of icons and a setup tool for idesk
License: GPL
Group: Graphical Desktop
Source: http://www.jmurray.id.au/idesk-extras-1.37.tgz
Source1: idesktool-zh_TW
BuildArch: noarch
Requires: idesk Xdialog

%description
A collection of icons plus a point'n'click
setup tool designed to help users get idesk
up and and running quickly and easily.

%prep
%setup -q -n home/john/tmp/%{name}-%{version}

%build

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_bindir}
%__mkdir_p %{buildroot}%{_datadir}/idesk
#cd home/john/tmp/%{name}-%{version}
%__cp %{SOURCE1} %{buildroot}%{_bindir}/idesktool
%__rm -rf icons/32x32/.xvpics icons/48x48/.xvpics
%__cp -a icons %{buildroot}%{_datadir}/idesk

%clean
%__rm -rf %{buildroot}

%files
%doc CHANGES COPYING idesk-extras.html
%{_datadir}/idesk/*
%{_bindir}/*

%changelog
* Mon Mar 05 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.37
- Rebuilt for Fedora
