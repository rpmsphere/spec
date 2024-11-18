Summary:        Runway, taxiway and AI traffic routing editor
Name:           taxidraw
Version:        0.3.2
Release:        6.1
License:        GPL
URL:            https://taxidraw.sourceforge.net/
Group:          Amusements/Games/3D/Simulation
Source0:        taxidraw-1317104301.tar.bz2
#Source0:        TaxiDraw-%{version}-src.tar.gz
Source1:        TaxiDraw.desktop
Source2:        TaxiDraw.png
Patch0:         taxidraw_initvars.patch
BuildRequires: desktop-file-utils
BuildRequires: gcc, gcc-c++, automake
BuildRequires: wxGTK2-devel
BuildRequires: curl-devel
BuildRequires: boost-devel >= 1.37

%description
TaxiDraw is an airport runway, taxiway, startup location, and AI traffic routing editor
for the FlightGear flight simulator.

%prep
%setup -q -n taxidraw-1317104301 -T -b 0
#setup -q -n TaxiDraw-%{version}
%patch 0 -p1
sed -i 's|HUGE|std::numeric_limits<double>::max()|' src/AI/AINetworkVerifier.cpp

%build
export CFLAGS="$RPM_OPT_FLAGS -fpermissive"
export CXXFLAGS="$RPM_OPT_FLAGS -fpermissive"
./autogen.sh
./configure --prefix=/usr
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make %{?_smp_mflags} install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps/.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/.

%files
%{_bindir}/*
%{_datadir}/pixmaps/TaxiDraw.png
%{_datadir}/applications/TaxiDraw.desktop

%changelog
* Tue Aug 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.2git
- Rebuilt for Fedora
* Fri Jan 20 2012 thorstenb@flightgear.org
- Created
