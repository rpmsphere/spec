%undefine _missing_build_ids_terminate_build
%undefine _debugsource_packages

Name:          joss
Version:       0.5
Release:       7.1
Summary:       An OSS emulator for Jack Audio Connection Kit
Group:         Applications/Multimedia
URL:           https://konstruktiv.org/software/joss
Source:        https://konstruktiv.org/software/joss/joss-%{version}.tar.bz2
License:       GPL
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libsamplerate-devel

%description
An OSS emulator for Jack Audio Connection Kit.

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -D -m0755 joss.so $RPM_BUILD_ROOT%{_libdir}/joss.so
sed -i 's|jossdir=/usr/local|jossdir=%{_prefix}|' joss
install -D -m0755 joss $RPM_BUILD_ROOT%{_bindir}/joss

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/joss
%{_libdir}/joss.so
%doc AUTHORS README

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5
- Rebuilt for Fedora
* Sat Sep 27 2008 Silvan Calarco <silvan.calarco@mambasoft.it> 0.5-1mamba
- package created by autospec
