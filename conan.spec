%global appsum The open-source C/C++ package manager
%global appdesc A distributed, open source, package manager for C/C++

Name: conan
Version: 0.30.3
Release: 1%{?dist}
Summary: %{appsum}

License: MIT
URL: https://github.com/conan-io/%{name}
Source0: %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: python2-devel
BuildRequires: python3-devel

BuildRequires: python2dist(requests)
BuildRequires: python3dist(requests)
BuildRequires: python2dist(six)
BuildRequires: python3dist(six)
BuildRequires: python2dist(colorama)
BuildRequires: python3dist(colorama)
#BuildRequires: python2dist(patch)
#BuildRequires: python3dist(patch)
BuildRequires: python2dist(fasteners)
BuildRequires: python3dist(fasteners)
BuildRequires: python2dist(semver)
BuildRequires: python3dist(semver)
BuildRequires: python2dist(distro)
BuildRequires: python3dist(distro)
BuildRequires: python2dist(pylint)
BuildRequires: python3dist(pylint)
BuildRequires: python2dist(future)
BuildRequires: python3dist(future)
BuildRequires: python2dist(pygments)
BuildRequires: python3dist(pygments)
BuildRequires: python2dist(astroid)
BuildRequires: python3dist(astroid)
BuildRequires: python2dist(pluginbase)
BuildRequires: python3dist(pluginbase)
BuildRequires: python2dist(bottle)
BuildRequires: python3dist(bottle)

BuildRequires: PyYAML
BuildRequires: python3-PyYAML
BuildRequires: python2-jwt
BuildRequires: python3-jwt

%description
%{appdesc}.

%package -n python2-%{name}
Summary: %{appsum}
Requires: python2dist(requests)
Requires: python2dist(six)
Requires: python2dist(requests)
Requires: python2dist(colorama)
Requires: python2dist(fasteners)
Requires: python2dist(semver)
Requires: python2dist(distro)
Requires: python2dist(pylint)
Requires: python2dist(future)
Requires: python2dist(pygments)
Requires: python2dist(astroid)
Requires: python2dist(pluginbase)
Requires: python2dist(bottle)
Requires: PyYAML
Requires: python2-jwt
%{?python_provide:%python_provide python2-%{name}}

%description -n python2-%{name}
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
Requires: python2-jwt
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
%{appdesc}.

%prep
%autosetup -n %{name}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{name}
%license LICENSE.md
%doc README.rst
%{python2_sitelib}/*

%files -n python3-%{name}
%license LICENSE.md
%doc README.rst
%{_bindir}/%{name}*
%{python3_sitelib}/*

%changelog
* Mon Dec 18 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0.30.3-1
- Initial SPEC release.
