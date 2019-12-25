%global appsum The open-source C/C++ package manager
%global appdesc A distributed, open source, package manager for C/C++

Name: conan
Version: 1.21.0
Release: 1%{?dist}
Summary: %{appsum}

License: MIT
URL: https://github.com/conan-io/%{name}
Source0: %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: python3-devel

BuildRequires: python3dist(requests)
BuildRequires: python3dist(six)
BuildRequires: python3dist(colorama)
#BuildRequires: python3dist(patch)
BuildRequires: python3dist(fasteners)
BuildRequires: python3dist(semver)
BuildRequires: python3dist(distro)
BuildRequires: python3dist(pylint)
BuildRequires: python3dist(future)
BuildRequires: python3dist(pygments)
BuildRequires: python3dist(astroid)
BuildRequires: python3dist(pluginbase)
BuildRequires: python3dist(bottle)

BuildRequires: PyYAML
BuildRequires: python3-PyYAML
BuildRequires: python3-jwt

%description
%{appdesc}.

%package -n python3-%{name}
Summary: %{appsum}
Requires: python3dist(requests)
Requires: python3dist(six)
Requires: python3dist(requests)
Requires: python3dist(colorama)
Requires: python3dist(fasteners)
Requires: python3dist(semver)
Requires: python3dist(distro)
Requires: python3dist(pylint)
Requires: python3dist(future)
Requires: python3dist(pygments)
Requires: python3dist(astroid)
Requires: python3dist(pluginbase)
Requires: python3dist(bottle)
Requires: python3-PyYAML
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
%{appdesc}.

%prep
%autosetup -n %{name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{name}
%license LICENSE.md
%doc README.rst
%{_bindir}/%{name}*
%{python3_sitelib}/*

%changelog
* Wed Dec 25 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 1.21.0-1
- Updated to version 1.21.0.
