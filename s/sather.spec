%undefine _debugsource_packages

Name: sather
Summary: GNU Sather programming language
Version: 1.2.3
Release: 8.1
Group: Development/Languages
License: GPL
URL: http://www.gnu.org/software/sather/
Source0: http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
BuildRequires: gc-devel

%description
Sather is an object oriented language which designed to be simple,
efficient, safe, and non-proprietary. It aims to meet the needs of
modern research groups and to foster the development of a large,
freely available, high-quality library of efficient well-written
classes for a wide variety of computational tasks.

%prep
%setup -q

%build
make -i
sed -i '1,45d' System/Common/CONFIG
sed -i '/isnormal/d' System/Common/runtime.h
make %{?_smp_mflags}

%install
install -d %{buildroot}%{_sysconfdir}/profile.d
echo "setenv SATHER_HOME /usr/share/sather" > %{buildroot}%{_sysconfdir}/profile.d/%{name}.csh
echo "export SATHER_HOME=/usr/share/sather" > %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh
install -d %{buildroot}%{_bindir}
install -m755 Bin/{gen_html,PP,sacomp,saprep} %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/%{name}
cp -a Emacs Library pLibrary System %{buildroot}%{_datadir}/%{name}

%files
%doc Doc/*
%attr(755,root,root) %{_sysconfdir}/profile.d/%{name}.*
%{_bindir}/*
%{_datadir}/%{name}

%changelog
* Thu Dec 27 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.3
- Rebuilt for Fedora
