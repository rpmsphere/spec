%undefine _auto_set_build_flags

BuildRequires:          kernel-devel
Name:                   setcd
Version:                1.5
Summary:                Control the behaviour of your cdrom device
License:                GPLv2
URL:                    https://www.elseware.nl/linux/setcd/
Group:                  Hardware/Other
Release:                8.1
Source:                 %{name}-%{version}.tar.gz
Patch0:                 %{name}-%{version}.diff.gz
Patch1:                 %{name}-%{version}.limits.diff
Patch2:                 %{name}-%{version}.Makefile.diff

%description
This program allows you to control the behaviour of your Linux cdrom player.

You can control: auto close, auto eject, medium type checking and tray/caddy
locking. You can get information on the volume name of CD-ROMs and other
data, and you can set the speed of your drive and choose a disc from a
jukebox.

The source of this package may be an example for cdrom player program
developers that wish to exploit the features of the linux cdrom interface.

%prep
%setup -q
%patch 0 -p1
%patch 1
%patch 2

%build
%{__make} %{?jobs:-j%jobs}

%install
%{__rm} -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1/
install -m 755 %{name} $RPM_BUILD_ROOT/%{_bindir}
install -m 644 %{name}.1 $RPM_BUILD_ROOT/%{_mandir}/man1/

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%doc README
%doc ChangeLog
%doc COPYRIGHT

%changelog
* Tue Aug 07 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5
- Rebuilt for Fedora
