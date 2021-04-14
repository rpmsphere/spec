%undefine _missing_build_ids_terminate_build

Summary:        Speech Synthesis System
Summary(de):    Sprachsynthese System
Name:           mbrola
Version:        302b
Release:        1.16
License:        see readme.txt
Group:          Productivity/Text/Convertors
URL:            https://github.com/numediart/MBROLA
Source0:        mbrola.tar
Source2:        txt2pho.zip
Source3:        say
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
%setup -qn MBROLA -a 0 -a 2

%build
make

%install
%{__mkdir_p} ${RPM_BUILD_ROOT}/etc
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_bindir}
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_datadir}/mbrola
%{__install} -m 755 ./Bin/mbrola ${RPM_BUILD_ROOT}%{_bindir}/mbrola

cat txt2pho/txt2phorc | sed -e "s/\/home\/tpo\/txt2pho\/data\//\/usr\/share\/mbrola\/data\//g" > ${RPM_BUILD_ROOT}/etc/txt2pho
cd txt2pho
%{__install} -m 755 txt2pho ${RPM_BUILD_ROOT}%{_bindir}/
mv data ${RPM_BUILD_ROOT}%{_datadir}/mbrola/
cd pipefilt
g++ ${RPM_OPT_FLAGS} pipefilt.cc -o pipefilt
%{__install} -m 755 pipefilt ${RPM_BUILD_ROOT}%{_bindir}/
cd ../preproc/
%{__make}
%{__install} -m 755 preproc ${RPM_BUILD_ROOT}%{_bindir}/
%{__install} -m 644 Rules.lst ${RPM_BUILD_ROOT}%{_datadir}/mbrola/
%{__install} -m 644 Hadifix.abk ${RPM_BUILD_ROOT}%{_datadir}/mbrola/
%{__install} -m 755 %{SOURCE3} ${RPM_BUILD_ROOT}%{_bindir}/

%clean
%{__rm} -rf ${RPM_BUILD_ROOT}

%files
%doc README.md
%license LICENSE
%config(noreplace) /etc/txt2pho
%{_bindir}/*
%dir %{_datadir}/mbrola
%dir %{_datadir}/mbrola/data
%{_datadir}/mbrola/*

%changelog
* Sat Apr 3 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 302b
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
