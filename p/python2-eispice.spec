Summary:  Python SPICE simulator
Name:     python2-eispice
Version:  0.11.6git
Release:  1
License:  Other (See Source)
Group:    Science
#Source:   eispice-0.11.6.tar.bz2
Source:   eispice-master.zip
URL:      http://www.thedigitalmachine.net/eispice.html
Vendor:   thedigitalmachine
Patch:    eispice-0.11.6.patch
BuildRequires: gcc-gfortran python2-devel tk-devel tcl-devel python2-numpy atlas-devel

%description
eispice is a clone of the Berkley SPICE 3 Simulation Engine. It was originally
targeted toward PCB level Signal Integrity Simulation; simulating IBIS model
defined devices, transmission lines, and passive termination but the scope of
the tool has been slowly expanding to include more general purpose circuit
simulation features.

%prep
%setup -qn eispice-master
%patch -p1
sed -i "s|'./include',|'./include', './libs/simulator/include',|" setup.py

%build
python2 setup.py build

%install
python2 setup.py install \
            --root="$RPM_BUILD_ROOT" \
            --prefix="%{_prefix}"

%files
%{python2_sitearch}/eispice.pth
%dir %{python2_sitearch}/eispice
%{python2_sitearch}/eispice/*

%changelog
* Sun Sep 18 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.11.6git
- Rebuilt for Fedora
