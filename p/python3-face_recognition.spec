%global srcname face_recognition

Name:           python3-%{srcname}
Version:        0.2.2
Release:        3.1
Summary:        The world's simplest facial recognition api for Python and the command line
License:        MIT
URL:            https://github.com/ageitgey/face_recognition
Source0:        https://github.com/ageitgey/face_recognition/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
BuildRequires:  python3-devel
Requires:       python3-dlib
Requires:       python3-scipy
Requires:       python3-click
Requires:       python3-pillow
Requires:       python3-face_recognition_models
BuildArch:      noarch

%description
Recognize and manipulate faces from Python or from the command line with the
world's simplest face recognition library. Built using dlib's state-of-the-art
face recognition built with deep learning. The model has an accuracy of 99.38%%
on the Labeled Faces in the Wild benchmark.

%prep
%setup -q -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files
%doc *.rst LICENSE
%{_bindir}/%{srcname}
%{python3_sitelib}/*

%changelog
* Wed Aug 01 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.2
- Rebuilt for Fedora
