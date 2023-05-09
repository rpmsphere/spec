BuildRequires: gcc-gfortran python2-devel tk-devel tcl-devel numpy atlas-devel
Summary:  Python SPICE simulator
Name:     python2-eispice
Version:  0.11.6
Release:  7.1
License:  Other (See Source)
Group:    Science
Source:   eispice-0.11.6.tar.bz2
URL:      http://www.thedigitalmachine.net/eispice.html
Vendor:   thedigitalmachine
Patch0:   eispice-0.11.6.patch

%description
eispice is a clone of the Berkley SPICE 3 Simulation Engine. It was originally
targeted toward PCB level Signal Integrity Simulation; simulating IBIS model
defined devices, transmission lines, and passive termination but the scope of
the tool has been slowly expanding to include more general purpose circuit
simulation features.

%prep
%setup -qn eispice-0.11.6
%patch0 -p1

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
* Wed Dec 28 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.11.6
- Rebuilt for Fedora
