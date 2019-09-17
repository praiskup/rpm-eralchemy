%global sum Entity Relation Diagrams generation tool
%global desc \
ERAlchemy generates Entity Relation (ER) diagram (like the one below) from \
databases or from SQLAlchemy models.
%global srcname ERAlchemy

Name:           eralchemy
Version:        1.2.10
Release:        2%{?dist}
Summary:        %{sum}

License:        ASL 2.0
URL:            https://github.com/Alexis-benoist/eralchemy
Source0:        %pypi_source

BuildArch:      noarch

Requires:       python3-%name = %version-%release

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%desc


%package -n python3-%name
Summary:        %sum

%description -n python3-%name
%desc


%prep
%autosetup -p1 -n %srcname-%version


%build
%py3_build


%install
%py3_install


%check


%files
%doc readme.md
%_bindir/eralchemy


%files -n python3-%name
%python3_sitelib/ERAlchemy-%version-*.egg-info
%python3_sitelib/eralchemy/*.py
%python3_sitelib/eralchemy/__pycache__


%changelog
* Tue Sep 17 2019 Pavel Raiskup <praiskup@redhat.com> - 1.2.10-2
- keep the %%_bindir script only in 'eralchemy' package (rhbz#1750263)

* Wed Sep 11 2019 Pavel Raiskup <praiskup@redhat.com> - 1.2.10-1
- apply review fixes (rhbz#1750263)

* Mon Sep 09 2019 Pavel Raiskup <praiskup@redhat.com> - 1.2.10-0
- initial RPM packaging
