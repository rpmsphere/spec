%undefine _missing_build_ids_terminate_build
%global tver 0.96

Summary:        Speech Synthesis System
Summary(de):    Sprachsynthese System
Name:           mbrola
Version:        3.3
Release:        1
License:        see readme.txt
Group:          Productivity/Text/Convertors
URL:            https://github.com/numediart/MBROLA
Source0:        MBROLA-%{version}.tar.gz
Source2:        https://github.com/GHPS/txt2pho/archive/%{tver}.tar.gz#/txt2pho-%{tver}.tar.gz
Source3:        say
Source4:        txt2phorc
Patch0:         txt2pho-gcc11.patch
BuildRequires:  glibc-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  unzip
Requires:       sox
#Recommends:     mbrola-de6

%description
Speech Synthesis System.
For german speech output install one or more of the mbrola-de packages.

%description -l de
Sprachsynthese System.
Für deutsche Sprachausgabe installieren Sie eines oder mehrere der
mbrola-de Pakete.

%prep
%setup -qn MBROLA-%{version} -a 0 -a 2
%patch 0 -p1
mkdir txt2pho-%{tver}/lib txt2pho-%{tver}/obj
sed -i 's/SYNTH_VERSION.*/SYNTH_VERSION \"%{version}\"/' Misc/common.h

%build
make
cd txt2pho-%{tver}
make

%install
%{__mkdir_p} ${RPM_BUILD_ROOT}/etc
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_bindir}
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_datadir}/mbrola
%{__install} -m 755 ./Bin/mbrola ${RPM_BUILD_ROOT}%{_bindir}/mbrola

cd txt2pho-%{tver}
install -m 755 txt2pho %{buildroot}%{_bindir}/
cp -r data %{buildroot}%{_datadir}/mbrola/
install -m 755 pipefilt %{buildroot}%{_bindir}/
install -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/txt2pho
install -m 755 preproc %{buildroot}%{_bindir}/
install -m 644 data/PPRules/rules.lst %{buildroot}%{_datadir}/mbrola/
install -m 644 data/hadifix.abk %{buildroot}%{_datadir}/mbrola/
install -m 755 %{SOURCE3} %{buildroot}%{_bindir}/

%files
%doc README.md
%license LICENSE
%config(noreplace) /etc/txt2pho
%{_bindir}/*
%{_datadir}/mbrola

%changelog
* Sun Oct 16 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 3.3
- Rebuilt for Fedora
* Thu Jul 04 2019 Bernhard M. Wiedemann <bernhard+packman lsmod de>
- build from source
- do not use dropped recode in 'say' script
* Mon Aug 29 2016 Bernhard M. Wiedemann <bernhard+packman lsmod de>
- Require sox for "play" tool used in say script (boo#995740)
* Sat Sep 05 2009 Manfred.Tremmel <Manfred.Tremmel@iiv.de> - 301h-1.pm.1
- cleanups where rpmlint wasn't so happy
* Tue Nov 01 2005 Manfred Tremmel <Manfred.Tremmel@iiv.de>
- first release
