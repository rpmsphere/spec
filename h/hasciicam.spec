Name: hasciicam
Summary: (h)ascii for the masses
Version: 1.3
Release: 5.1
Group: Applications/Graphics
License: GPLv3
URL: http://ascii.dyne.org/
Source0: %{name}_%{version}.tar.gz
Patch0: hasciicam_1.3_returns.patch
BuildRequires: aalib-devel
BuildRequires: ftplib-devel

%description
Hasciicam makes it possible to have live ASCII video on the web. It
captures video from a tv card and renders it into ascii, formatting the
output into an html page with a refresh tag or in a live ASCII window or
in a simple text file as well, giving the possibility to anybody that has a
bttv card, a Linux box and a cheap modem line to show a live ASCII video
feed that can be browsable without any need for plugin, java etc.

%prep
%setup -q -n %{name}_%{version}
%patch0 -p1

%build
%configure
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{_datadir}/menu/hasciicam
mv %{buildroot}%{_datadir}/icons %{buildroot}%{_datadir}/pixmaps

%files
%doc TODO README NEWS COPYING ChangeLog AUTHORS
%{_bindir}/*
%{_mandir}/man?/%{name}.?.*
%{_datadir}/applications/hasciicam.desktop
%{_datadir}/pixmaps/hasciicam.png

%changelog
* Mon Jan 08 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3
- Rebuilt for Fedora
