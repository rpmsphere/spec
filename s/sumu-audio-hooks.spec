%undefine _debugsource_packages
Summary:   Audio hooks for SUMU
Name:      sumu-audio-hooks
Version:   0.2
Release:   1
URL:       https://code.google.com/p/otb-sources/wiki/SUMU
License:   LGPLv2+
Group:     System Environment/Base
Source0:   pactl_list.c
Source1:   Makefile-%{name}
Source2:   COPYING-%{name}
Source3:   sumu-init.sh
BuildRequires: pulseaudio-libs-devel

%description
Audio hooks for the SUMU project. This package configures default
audio preferences and without it there will be no sound available.

%prep
%setup -T -c
cp %{SOURCE0} .
cp %{SOURCE1} Makefile

%build
make compile %{?_smp_mflags}

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_docdir}/%{name}-%{version}
install -m 0644 %{SOURCE2} %{buildroot}/%{_docdir}/%{name}-%{version}/COPYING

mkdir -p %{buildroot}/%{_bindir}
install -m 0755 pactl_list %{buildroot}/%{_bindir}/

mkdir -p %{buildroot}/%{_sysconfdir}/profile.d
install -m 0644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/profile.d

%clean
rm -rf %{buildroot}

%files
%config(noreplace) %{_sysconfdir}/profile.d/sumu-init.sh
%doc %{_docdir}/%{name}-%{version}/
%{_bindir}/pactl_list

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuilt for Fedora
* Fri Mar 04 2011 Alexander Todorov <atodorov@NO-SPAM.otb.bg> 0.2-1.el6otb
- don't execute sumu-init.sh if no /dev/usbseat is present
- don't loop over all seats when we've found what we need
* Tue Feb 22 2011 Alexander Todorov <atodorov@NO-SPAM.otb.bg> 0.1-1.el6otb
- initial revision
