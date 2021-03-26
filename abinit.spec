Summary: Computational Chemistry DFT program
Name: abinit
Version: 8.10.1
Release: 1
License: GPL
Group: Sciences/Chemistry
URL: http://www.abinit.org/
Source: http://ftp.abinit.org/abinit-%{version}.tar.gz
BuildRequires: gcc-gfortran

%description
ABINIT is a package whose main program allows one to find the total energy,
charge density and electronic structure of systems made of electrons and
nuclei (molecules and periodic solids) within Density Functional Theory (DFT),
using pseudopotentials and a planewave basis. ABINIT also includes options
to optimize the geometry according to the DFT forces and stresses, or
to perform molecular dynamics simulations using these forces, or to generate
dynamical matrices, Born effective charges, and dielectric tensors. Excited
states can be computed within the Time-Dependent Density Functional Theory
(for molecules), or within Many-Body Perturbation Theory (the GW
approximation). In addition to the main ABINIT code, different utility
programs are provided.

%prep
%setup -q
#sed -i -e '225s|12|33|' -e '347s|12|33|' src/67_common/m_vcoul.F90
sed -i "s|I did my best but I failed. Sorry. ||" src/46_diago/m_lobpcg2.F90
sed -i "s|don't sum up to one but to||" src/56_recipspace/m_lgroup.F90
sed -i -e "s|in order to compute the gkk||" -e "s|code does not yet support||" -e "s|, model GW with nspinor 2 are||" -e "s| when performing EPH calculations||" src/57_iovars/m_chkinp.F90
sed -i "s| rf2_apply_hamiltonian can be used ||" src/72_response/m_rf2.F90
sed -i "s|the number of threads to something close ||" src/79_seqpar_mpi/m_lobpcgwf.F90
sed -i "s|The basis of atoms written in input.in file ||" src/80_tdep/m_tdep_utils.F90
sed -i "s| This is not coded yet. Imag part ignored||" src/94_scfcv/m_outscfcv.F90
sed -i -e "s|, which is not the case here||" -e "s| with at most one phonon perturbation||" src/95_drive/m_dfptnl_loop.F90
sed -i "s| at the moment just for insulators and norm-conserving psp||" src/95_drive/m_respfn_driver.F90
sed -i "s|must contain both uniaxial and shear strain ||" src/98_main/anaddb.F90
    
%build
%configure
sed -i 's|-Wall|-Wall -Wno-error|' Makefile */Makefile */*/Makefile
make

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%doc doc/tutorial
%{_bindir}/*
%{_libdir}/pkgconfig/*
%{_datadir}/*

%changelog
* Wed Dec 26 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 8.10.1
- Rebuild for Fedora
* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 6.0.4-alt1.qa1
- NMU: rebuilt for debuginfo.
* Tue Jun 01 2010 Ilya Mashkin <oddity@altlinux.ru> 6.0.4-alt1
- 6.0.4
* Tue Aug 11 2009 Ilya Mashkin <oddity@altlinux.ru> 5.8.4-alt1
- 5.8.4
* Sat Jan 10 2009 Ilya Mashkin <oddity@altlinux.ru> 5.6.4-alt1
- 5.6.4
- spec cleanup
* Mon Jul 10 2006 Andrey Khavryuchenko <akhavr@altlinux.org> 4.6.5-alt1
- Initial build
